from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: str
    price: float = Field(gt=0)
    description: str
    rating: float = Field(ge=0, le=5, default=0.0)
    image_url: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    image_url: Optional[str] = None

class ProductSearch(BaseModel):
    query: Optional[str] = None
    category: Optional[str] = None
    min_price: Optional[float] = Field(None, ge=0)
    max_price: Optional[float] = Field(None, gt=0)
    min_rating: Optional[float] = Field(None, ge=0, le=5) 