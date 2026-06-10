"""Auction and Bidding Models"""

from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base


class AuctionStatus(str, PyEnum):
    """Auction statuses"""
    SCHEDULED = "scheduled"
    ACTIVE = "active"
    CLOSED = "closed"
    SOLD = "sold"
    CANCELLED = "cancelled"


class Auction(Base):
    """Auction Model"""
    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    
    starting_bid = Column(Float, nullable=False)
    current_bid = Column(Float)
    reserve_price = Column(Float)
    
    status = Column(Enum(AuctionStatus), default=AuctionStatus.SCHEDULED)
    
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    
    winner_id = Column(Integer, ForeignKey("users.id"))
    final_price = Column(Float)
    
    is_auto_extend = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    product = relationship("Product", back_populates="auctions")
    seller = relationship("User", foreign_keys=[seller_id])
    winner = relationship("User", foreign_keys=[winner_id])
    bids = relationship("Bid", back_populates="auction", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Auction {self.title}>"


class Bid(Base):
    """Bid Model"""
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, index=True)
    auction_id = Column(Integer, ForeignKey("auctions.id"), nullable=False)
    bidder_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    amount = Column(Float, nullable=False)
    is_auto_bid = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relationships
    auction = relationship("Auction", back_populates="bids")
    bidder = relationship("User", back_populates="bids")
    
    def __repr__(self):
        return f"<Bid {self.amount}>"
