import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "Inventory Management API")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:////app/instance/inventory.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "false").lower() == "true"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "1234567890")

    # Default admin
    ADMIN_USER = os.getenv("ADMIN_USER", "admin")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
    ADMIN_PASS = os.getenv("ADMIN_PASS", "adminpassword")

    # Blacklist configuration
    JWT_BLACKLIST_ENABLED = os.getenv("JWT_BLACKLIST_ENABLED", "true").lower() == "true"
    JWT_BLACKLIST_TOKEN_CHECKS = os.getenv("JWT_BLACKLIST_TOKEN_CHECKS", '["access", "refresh"]')

    # Swagger configuration
    SWAGGER_URL = os.getenv("SWAGGER_URL", "/api/docs")
    API_URL = os.getenv("API_URL", "../public/swagger.yaml")
