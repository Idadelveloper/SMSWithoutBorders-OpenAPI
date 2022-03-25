import logging
from flask import Flask
from configparser import ConfigParser
from routes.v1 import v1
from flask_swagger_ui import get_swaggerui_blueprint

config = ConfigParser()
config.read("config/default.ini")

api = config["API"]

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/v1/api-docs", "/static/v1-api-docs.json"
)

app.register_blueprint(swaggerui_blueprint)

app.register_blueprint(v1, url_prefix="/v1")

if __name__ == "__main__":
    app.run(port=api["PORT"])