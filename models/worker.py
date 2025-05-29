from sqlalchemy import Column, Integer, String, Enum, Date, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base
from enums import Role

class Worker(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(Enum(Role), nullable=False)
    phone = Column(String(20))
    hire_date = Column(Date)
    salary = Column(DECIMAL(10, 2), nullable=False)

    payrolls = relationship("Payroll", back_populates="worker")
    deliveries = relationship("Delivery", back_populates="worker")
