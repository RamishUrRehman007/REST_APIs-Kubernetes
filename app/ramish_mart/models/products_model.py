import uuid, datetime
from ramish_mart import db

class Products(db.Model):

    id = db.Column(db.String(100), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False) 
    created = db.Column(db.DateTime(), default=datetime.datetime.utcnow())

    def __init__(self, name, price):
        self.name = name
        self.price = price

db.create_all()

def get_product_object(name):
    return Products.query.filter_by(name=name).first()