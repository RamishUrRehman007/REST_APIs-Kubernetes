from flask import jsonify, request
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token

from ramish_mart import app, username, password
from ramish_mart.utils import utils

@cross_origin
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data  = utils.posted()
        if data['username'] == username and data['password'] == password:
            access_token = create_access_token(identity=username)
            return jsonify(
                        utils.form_response(200, 'Authenticated, Token Generated', { "token": access_token, "user_id": username})
                    ), 200 
        else:
            return jsonify(
                        utils.form_response(401, 'Bad username or password', None)
                    ), 401

    else:
        return jsonify(
                        utils.form_response(405, 'Method Not Allowed', None)
                    ), 405