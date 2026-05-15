from flask import Flask, jsonify, request
from database import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def home():
    return "E-shop API"

from customers import Customer

@app.route("/customers", methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers])

from orders import Order

@app.route("/orders", methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders])

@app.route("/orders/<int:order_id>", methods=['GET'])
def get_order_id(order_id):
    order = Order.query.get(order_id)
    return jsonify(order.to_dict())

@app.route("/customers/<int:customer_id>/orders", methods=['GET'])
def get_customer_orders(customer_id):
    orders = Order.query.filter_by(customer_id=customer_id).all()
    return jsonify([o.to_dict() for o in orders])

@app.route("/customers/<int:customer_id>/orders", methods=['POST'])
def create_order(customer_id):
    data = request.get_json()
    order = Order(customer_id=customer_id, product_name=data['product_name'], quantity=data['quantity'])
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201

@app.route("/orders/<int:order_id>", methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    data = request.get_json()
    order.product_name = data['product_name']
    order.quantity = data['quantity']
    db.session.commit()
    return jsonify(order.to_dict())

@app.route("/orders/<int:order_id>", methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'objednavka zmazana'})


if __name__ == '__main__':
    app.run(debug=True)
