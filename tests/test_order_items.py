from models.order_item import OrderItem
from models.product import Product
from models.order import Order
from models.customer import Customer

def test_order_item_relationships(db_session):
    customer = Customer(name="Bob")
    product = Product(name="Croissant", price=3.00)
    order = Order(customer=customer, total_amount=0)
    db_session.add_all([customer, product, order])
    db_session.commit()

    item = OrderItem(order=order, product=product, quantity=3, unit_price=3.00)
    db_session.add(item)
    db_session.commit()

    assert item.order.customer.name == "Bob"
    assert item.product.name == "Croissant"
