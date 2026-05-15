import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_customers(client):
    response = client.get('/customers')
    assert response.status_code == 200

def test_get_orders(client):
    response = client.get('/orders')
    assert response.status_code == 200

def test_get_order_not_found(client):
    response = client.get('/orders/99999')
    assert response.status_code == 404
