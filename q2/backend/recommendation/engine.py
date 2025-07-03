from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Dict
from ..models import Product, UserInteraction
from sqlalchemy.orm import Session

class RecommendationEngine:
    def __init__(self):
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.product_vectors = None
        self.product_ids = None
        self.similarity_matrix = None

    def _prepare_product_text(self, product: Product) -> str:
        """Combine product features into a single text string."""
        return f"{product.name} {product.category} {product.description}"

    def fit(self, products: List[Product]):
        """Train the recommendation engine on the product data."""
        # Prepare text data
        product_texts = [self._prepare_product_text(p) for p in products]
        self.product_ids = [p.id for p in products]

        # Create TF-IDF vectors
        self.product_vectors = self.tfidf.fit_transform(product_texts)
        
        # Calculate similarity matrix
        self.similarity_matrix = cosine_similarity(self.product_vectors)

    def get_similar_products(self, product_id: int, n: int = 5) -> List[int]:
        """Get n most similar products to the given product."""
        if product_id not in self.product_ids:
            return []

        # Get product index
        idx = self.product_ids.index(product_id)
        
        # Get similarity scores
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        
        # Sort products by similarity
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get top N similar products (excluding itself)
        sim_scores = sim_scores[1:n+1]
        
        # Return product IDs
        return [self.product_ids[i] for i, _ in sim_scores]

    def get_personalized_recommendations(
        self,
        user_id: int,
        db: Session,
        n: int = 5
    ) -> List[int]:
        """Get personalized recommendations based on user interactions."""
        # Get user's interactions
        interactions = db.query(UserInteraction).filter(
            UserInteraction.user_id == user_id
        ).all()

        if not interactions:
            # Return popular products if no interactions
            return self._get_popular_products(db, n)

        # Get weighted scores for each product based on interactions
        scores = np.zeros(len(self.product_ids))
        for interaction in interactions:
            if interaction.product_id in self.product_ids:
                idx = self.product_ids.index(interaction.product_id)
                # Weight: 1.0 for views, 2.0 for likes
                weight = 2.0 if interaction.type == 'like' else 1.0
                scores += self.similarity_matrix[idx] * weight

        # Get top N recommendations
        top_indices = scores.argsort()[-n:][::-1]
        return [self.product_ids[i] for i in top_indices]

    def _get_popular_products(self, db: Session, n: int = 5) -> List[int]:
        """Get most popular products based on interaction count."""
        popular_products = (
            db.query(UserInteraction.product_id)
            .group_by(UserInteraction.product_id)
            .order_by(db.func.count().desc())
            .limit(n)
            .all()
        )
        return [p[0] for p in popular_products]

# Global instance
recommendation_engine = RecommendationEngine() 