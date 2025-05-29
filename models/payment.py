from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime, Enum, func
from sqlalchemy.orm import relationship
from .base import Base
from enums import PaymentMethod

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    payment_date = Column(DateTime, default=func.now())
    amount_paid = Column(DECIMAL(10, 2))
    payment_method = Column(Enum(PaymentMethod))

    order = relationship("Order", back_populates="payments")
