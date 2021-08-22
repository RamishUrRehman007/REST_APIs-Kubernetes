from ramish_mart.utils import utils
from ramish_mart import db
from ramish_mart.models.products_model import Products, get_product_object

def addProduct(name, price):
    _product = Products(
            name=name,
            price=price
        )

    db.session.add(_product)
    db.session.commit()
    
    product = utils.single_object_to_dict(
                    Products.query.filter_by(name=name).first()
                )
    
    return {'Message': "Product Added Successfully" , 'Product' : product}