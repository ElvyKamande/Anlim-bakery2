from models.order import Order
from models.customer import Customer

def test_create_order_with_customer(db_session):
    customer = Customer(name="John", email="john@example.com")
    db_session.add(customer)
    db_session.commit()

    order = Order(customer_id=customer.id, total_amount=0)
    db_session.add(order)
    db_session.commit()

    assert order.customer_id == customer.id
