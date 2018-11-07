import os

from flask import Flask

from coffeechat.config import Config
from coffeechat.controllers import init_app_routes

app = Flask(__name__)
app.config.from_object(Config)

init_app_routes(app)