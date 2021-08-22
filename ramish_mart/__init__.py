from flask import Flask
from flask_log_request_id import RequestID, RequestIDLogFilter
from logging.handlers import TimedRotatingFileHandler
import logging, os

app = Flask(__name__)

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