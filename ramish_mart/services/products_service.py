from ramish_mart.utils import utils
from ramish_mart import db
from ramish_mart.models.products_model import Products, get_product_object

def addProduct(name, price):

    try:
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
    
    except Exception as e:
        return {'Message': str(e)}

def deleteProduct(product_id):

    try:
        Products.query.filter_by(
                        id=product_id
                    ).delete()
        db.session.commit()
        
        return {'Message': "Product Deleted Successfully"}
    
    except Exception as e:
        return {'Message': str(e)}
