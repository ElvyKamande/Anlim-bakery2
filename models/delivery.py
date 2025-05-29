from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from .base import Base
from enums import DeliveryStatus

class Delivery(Base):
    __tablename__ = 'deliveries'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    worker_id = Column(Integer, ForeignKey('workers.id'))
    delivery_time = Column(DateTime)
    status = Column(Enum(DeliveryStatus))

    order = relationship("Order", back_populates="delivery")
    worker = relationship("Worker", back_populates="deliveries")
