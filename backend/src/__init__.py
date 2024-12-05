from flask import Flask
from config import Config
from src.extensions import register_extensions, jwt
from src.tasks.token_cleanup import setup_token_cleanup_scheduler
from src.errors.handlers import register_error_handlers
from src.routes import register_routes
from src.commands import register_commands
from src.swagger.setup import register_swagger_api
from src.auth import register_auth


def create_app():
    """
    Create and configure the Flask application, including extensions, routes, and admin setup.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions like database, migrations, and JWT
    register_extensions(app)

    # Register CLI commands
    register_commands(app)

    # Register JWT handlers for token revocation and other JWT-specific logic
    register_auth(jwt)

    # Set up the token cleanup scheduler
    setup_token_cleanup_scheduler(app)

    # Register routes, error handlers, and Swagger API
    register_routes(app)
    register_error_handlers(app)
    register_swagger_api(app)

    return app
