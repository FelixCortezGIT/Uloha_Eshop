from flask import Flask, jsonify
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
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email} for c in customers])


# @app.route("/orders")
# def get_orders():


if __name__ == '__main__':
    app.run(debug=True)
