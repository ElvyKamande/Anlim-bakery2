from models.base import Base
from database import engine
import models.customer
import models.product
import models.order
import models.order_item
import models.payment
import models.worker
import models.payroll
import models.delivery

# Create all tables
Base.metadata.create_all(bind=engine)
print("✅ All tables created.")
