from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def register_extensions(app):
    """
    Initialize Flask extensions such as database, migration, and JWT.
    """
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)