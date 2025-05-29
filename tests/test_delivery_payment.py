from models.delivery import Delivery
from models.order import Order
from models.customer import Customer
from models.payment import Payment

def test_delivery_and_payment(db_session):
    customer = Customer(name="Sam")
    order = Order(customer=customer, total_amount=50.0)
    db_session.add_all([customer, order])
    db_session.commit()

    delivery = Delivery(order_id=order.id, status="pending")
    payment = Payment(order_id=order.id, amount=50.0, method="cash")
    db_session.add_all([delivery, payment])
    db_session.commit()

    assert delivery.order.id == order.id
    assert payment.amount == 50.0
