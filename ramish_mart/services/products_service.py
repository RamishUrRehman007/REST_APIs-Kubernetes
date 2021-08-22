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

def updateProduct(product_id, fields_to_be_updated):

    try:
        if 'id' in list(fields_to_be_updated.keys()) or  'created' in list(fields_to_be_updated.keys()):
            return False
        
        Products.query.filter_by(
                        id=product_id
                    ).update(fields_to_be_updated)
        db.session.commit()
        
        product = utils.single_object_to_dict(
                        Products.query.filter_by(id=product_id).first()
                    )
        
        return {'Message': "Product Updated Successfully" , 'Product' : product}
    
    except Exception as e:
        return {'Message': str(e)}


def getProductByName(product_name):

    try:
        product = utils.single_object_to_dict(
                        get_product_object(product_name)
                    )
        
        return {'Message': "Product Fetched Successfully" , 'Product' : product}
    
    except Exception as e:
        return {'Message': str(e)}