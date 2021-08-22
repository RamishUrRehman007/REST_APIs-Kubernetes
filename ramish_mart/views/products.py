from flask import jsonify
from flask_cors import cross_origin
from flask.globals import request

from ramish_mart import app
from ramish_mart.services import products_service
from ramish_mart.utils import utils

@cross_origin
@app.route("/products", methods=["GET", "POST", "DELETE", "PATCH"])
def products():
    if request.method == "POST":
        data  = utils.posted()
        if 'name' in data and 'price' in data:
            name = data['name']
            price = int(data['price'])

            product = products_service.addProduct(
                                        name, price
                                    )

            return jsonify(
                        utils.form_response(200, None, product)
                    ) 
        else:
            return jsonify(
                        utils.form_response(400, 'Keys are missing', None)
                    ) 

    elif request.method == "GET":
        product_name = request.args.get('name', None)
        
        if product_name:
            product = products_service.getProductByName(product_name)
            return jsonify(
                        utils.form_response(200, None, product)
                    )
        else:
            return jsonify(
                        utils.form_response(400, 'Query Param is missing-name', None)
                    )

    elif request.method == "DELETE":
        product_id = request.args.get('product_id', None)

        if product_id:
            product = products_service.deleteProduct(product_id)
            return jsonify(
                        utils.form_response(200, None, product)
                    ) 
        else:
            return jsonify(
                        utils.form_response(400, 'Query Param is missing-product_id', None)
                    ) 
    
    elif request.method == "PATCH":
        product_id = request.args.get('product_id', None)

        if product_id:
            fields_to_be_updated  = utils.posted()
            if fields_to_be_updated:
                product = products_service.updateProduct(
                                            product_id, fields_to_be_updated
                                        )
                if product == False:
                    return jsonify(
                            utils.form_response(403, 'Trying to update forbidden fields', None)
                        )
                
                return jsonify(
                            utils.form_response(200, None, product)
                        ) 
            else:
                return jsonify(
                            utils.form_response(400, 'Json Data is missing', None)
                        ) 
        else:
            return jsonify(
                        utils.form_response(400, 'Query Param is missing-product_id', None)
                    ) 