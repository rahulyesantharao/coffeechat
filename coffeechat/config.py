import os

class Config:
    APP_NAME = os.environ.get("APP_NAME", "coffeechat")
    PORT = os.environ.get("PORT", 8899)
    DEBUG = bool(os.environ.get("DEBUG", False))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", 'sqlite:///db')