"""Product Model"""

from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base


class ProductCategory(str, PyEnum):
    """Product categories"""
    ELECTRONICS = "electronics"
    REFURBISHED = "refurbished"
    RECYCLED = "recycled"
    NEW = "new"
    SECOND_HAND = "second_hand"
    COMPONENTS = "components"


class Product(Base):
    """Product Model"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    name = Column(String(255), index=True, nullable=False)
    description = Column(Text)
    sku = Column(String(100), unique=True, index=True)
    
    category = Column(Enum(ProductCategory), nullable=False)
    price = Column(Float, nullable=False)
    cost = Column(Float)
    stock = Column(Integer, default=0)
    
    image_url = Column(String(500))
    condition = Column(String(50))
    
    is_active = Column(Boolean, default=True)
    is_auction = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    vendor = relationship("User", back_populates="products", foreign_keys=[vendor_id])
    order_items = relationship("OrderItem", back_populates="product")
    auctions = relationship("Auction", back_populates="product")
    
    def __repr__(self):
        return f"<Product {self.name}>"
