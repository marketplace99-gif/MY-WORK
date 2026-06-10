"""User Model"""

from sqlalchemy import Column, String, Enum, Boolean, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base


class UserRole(str, PyEnum):
    """User roles"""
    ADMIN = "admin"
    VENDOR = "vendor"
    BUYER = "buyer"


class User(Base):
    """User Model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    phone = Column(String(20))
    address = Column(String(500))
    city = Column(String(100))
    country = Column(String(100))
    postal_code = Column(String(20))
    
    role = Column(Enum(UserRole), default=UserRole.BUYER, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    products = relationship("Product", back_populates="vendor", foreign_keys="Product.vendor_id")
    orders = relationship("Order", back_populates="buyer")
    bids = relationship("Bid", back_populates="bidder")
    
    def __repr__(self):
        return f"<User {self.email}>"
