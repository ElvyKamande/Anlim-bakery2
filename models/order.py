from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime, Enum
from sqlalchemy.orm import relationship
from .base import Base
from enums import OrderStatus

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime)
    total_amount = Column(DECIMAL(10, 2))
    status = Column(Enum(OrderStatus))

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    payments = relationship("Payment", back_populates="order")
    delivery = relationship("Delivery", back_populates="order", uselist=False)
