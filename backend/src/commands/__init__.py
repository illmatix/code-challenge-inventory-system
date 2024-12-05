from .seed import register_seed_command


def register_commands(app):
    """
    Registers all CLI commands for the Flask application.
    """
    register_seed_command(app)
