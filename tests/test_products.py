from models.product import Product

def test_create_product(db_session):
    product = Product(name="Chocolate Cake", price=15.99)
    db_session.add(product)
    db_session.commit()

    assert product.id is not None
    assert product.price == 15.99
