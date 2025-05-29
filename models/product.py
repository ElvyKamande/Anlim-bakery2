from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock_quantity = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())

    order_items = relationship("OrderItem", back_populates="product")
