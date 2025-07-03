from database import SessionLocal
from models import User, Product
from passlib.context import CryptContext

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_test_data():
    db = SessionLocal()
    try:
        # Create test user
        test_user = User(
            email="test@example.com",
            name="Test User",
            password_hash=pwd_context.hash("testpassword123")
        )
        db.add(test_user)

        # Create test products
        test_products = [
            Product(
                name="Test Product 1",
                category="Electronics",
                price=99.99,
                description="A test electronic product",
                rating=4.5,
                image_url="https://example.com/image1.jpg"
            ),
            Product(
                name="Test Product 2",
                category="Books",
                price=29.99,
                description="A test book product",
                rating=4.0,
                image_url="https://example.com/image2.jpg"
            )
        ]
        db.add_all(test_products)
        
        # Commit the changes
        db.commit()
        print("Test data created successfully!")
        
    except Exception as e:
        print(f"Error creating test data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_test_data() 