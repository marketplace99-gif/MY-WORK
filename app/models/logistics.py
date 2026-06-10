"""Logistics and Shipment Models"""

from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base


class ShipmentStatus(str, PyEnum):
    """Shipment statuses"""
    PENDING = "pending"
    PICKED = "picked"
    PACKED = "packed"
    SHIPPED = "shipped"
    IN_TRANSIT = "in_transit"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    FAILED = "failed"
    RETURNED = "returned"


class Shipment(Base):
    """Shipment/Logistics Model"""
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    
    tracking_number = Column(String(100), unique=True, index=True)
    carrier = Column(String(50))
    
    status = Column(Enum(ShipmentStatus), default=ShipmentStatus.PENDING)
    
    origin_address = Column(String(500))
    origin_city = Column(String(100))
    origin_country = Column(String(100))
    
    destination_address = Column(String(500))
    destination_city = Column(String(100))
    destination_country = Column(String(100))
    
    weight = Column(Float)
    dimensions = Column(String(50))
    
    shipping_cost = Column(Float)
    estimated_delivery = Column(DateTime)
    actual_delivery = Column(DateTime)
    
    latitude = Column(Float)
    longitude = Column(Float)
    
    notes = Column(String(500))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order = relationship("Order", back_populates="shipment")
    
    def __repr__(self):
        return f"<Shipment {self.tracking_number}>"
