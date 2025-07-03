from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Product
from ..auth.middleware import get_current_user
from ..recommendation.engine import recommendation_engine

router = APIRouter()

@router.get("/similar/{product_id}", response_model=List[Product])
def get_similar_products(
    product_id: int,
    n: int = 5,
    db: Session = Depends(get_db)
):
    """Get similar products based on content."""
    # Get all products to train/update the model
    products = db.query(Product).all()
    
    # Train recommendation engine
    recommendation_engine.fit(products)
    
    # Get similar product IDs
    similar_ids = recommendation_engine.get_similar_products(product_id, n)
    
    # Get product details
    similar_products = db.query(Product).filter(Product.id.in_(similar_ids)).all()
    return similar_products

@router.get("/personalized", response_model=List[Product])
def get_personalized_recommendations(
    n: int = 5,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get personalized recommendations based on user interactions."""
    # Get all products to train/update the model
    products = db.query(Product).all()
    
    # Train recommendation engine
    recommendation_engine.fit(products)
    
    # Get recommended product IDs
    recommended_ids = recommendation_engine.get_personalized_recommendations(
        current_user.id,
        db,
        n
    )
    
    # Get product details
    recommended_products = db.query(Product).filter(Product.id.in_(recommended_ids)).all()
    return recommended_products

@router.get("/popular", response_model=List[Product])
def get_popular_products(
    n: int = 5,
    db: Session = Depends(get_db)
):
    """Get most popular products."""
    # Get all products to train/update the model
    products = db.query(Product).all()
    
    # Train recommendation engine
    recommendation_engine.fit(products)
    
    # Get popular product IDs
    popular_ids = recommendation_engine._get_popular_products(db, n)
    
    # Get product details
    popular_products = db.query(Product).filter(Product.id.in_(popular_ids)).all()
    return popular_products 