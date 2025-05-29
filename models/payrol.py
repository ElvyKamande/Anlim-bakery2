from sqlalchemy import Column, Integer, ForeignKey, Date, Float, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base

class Payroll(Base):
    __tablename__ = 'payrolls'

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('workers.id'))
    pay_period_start = Column(Date)
    pay_period_end = Column(Date)
    hours_worked = Column(Float)
    total_pay = Column(DECIMAL(10, 2))
    payment_date = Column(Date)

    worker = relationship("Worker", back_populates="payrolls")
