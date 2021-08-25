from flask import Flask
from flask_jwt_extended import JWTManager
from flask_log_request_id import RequestID, RequestIDLogFilter
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import TimedRotatingFileHandler
import logging, os
from ramish_mart.config import config


app = Flask(__name__)

# --- Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "ramish-secret"  # Change this "ramish secret" with something else!
jwt = JWTManager(app)
# --- Setup the Flask-JWT-Extended extension

# --- set app logger
ramish_mart_LOG_LEVEL = logging.DEBUG
TEXT_ENCODING = "UTF-8"
RequestID(app)
app.log = logging.getLogger("ramish_mart")
app.log.setLevel(ramish_mart_LOG_LEVEL)
fmt = logging.Formatter(
    "%(asctime)s, [%(levelname)-8s], [%(request_id)s], %(message)s, in [%(filename)s:%(lineno)d]"
)
log_filename = "/log/ramish_mart.log"
if not os.path.exists(os.getcwd() + "/log/"):
    os.makedirs(os.getcwd() + "/log/")
file_handler = TimedRotatingFileHandler(
    os.getcwd() + log_filename, when="midnight", interval=1, encoding=TEXT_ENCODING
)
console_handler = logging.StreamHandler()
handlers = [file_handler, console_handler]
for handler in handlers:
    handler.setFormatter(fmt)
    handler.setLevel(ramish_mart_LOG_LEVEL)
    handler.addFilter(RequestIDLogFilter())
    app.log.addHandler(handler)
# --- set app logger

# --- Connect to DB
config_manager = config.register_config_manager()
DB_URI = "postgresql://"+config_manager.get("USERNAME")+":"+config_manager.get("PASSWORD")+"@"+config_manager.get("HOST_URL")+":"+config_manager.get("PORT")+"/"+config_manager.get("DATABASE_NAME")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# --- Connect to DB

# --- Set Username and Password for JWT 
username = config_manager.get("USERNAME")
password = config_manager.get("PASSWORD")
# --- Set Username and Password for JWT

# Initialize Models
from ramish_mart.models import (products_model)
# Initialize Models

# --- import views
from ramish_mart.views import(
                            test,
                            products,
                            login
                        )
# --- import views

# --- swagger specific
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Ramish-Test"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# --- swagger specific

#  docker build -t ramish-test .
#  docker-compose up --build -d  
# kubectl apply -f deployment.yaml
# kubectl rollout restart deployment 