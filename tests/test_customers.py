from models.customer import Customer

def test_create_customer(db_session):
    customer = Customer(name="Jane Doe", email="jane@example.com", phone="1234567890")
    db_session.add(customer)
    db_session.commit()

    assert customer.id is not None
    assert db_session.query(Customer).count() == 1
