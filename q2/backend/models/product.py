from sqlalchemy import Column, Integer, String, Float, Text
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Float)
    description = Column(Text)
    rating = Column(Float, default=0.0)
    image_url = Column(String)

    def __repr__(self):
        return f"<Product {self.name}>" 