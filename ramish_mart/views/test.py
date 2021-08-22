from flask import jsonify
from ramish_mart import app

@app.route("/")
def index_view():
    return jsonify(message="Success")