from database import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.Date, server_default='CURRENT_DATE')

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "order_date": str(self.order_date)
        }
