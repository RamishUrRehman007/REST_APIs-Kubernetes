from flask import jsonify
from flask_cors import cross_origin
from flask.globals import request

from ramish_mart import app
from ramish_mart.services import products_service
from ramish_mart.utils import utils

@cross_origin
@app.route("/products", methods=["POST", "DELETE"])
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
    
    