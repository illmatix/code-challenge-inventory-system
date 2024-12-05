import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, timezone
from src.extensions import db


class User(db.Model):
    """
    Represents application users, including their authentication details and roles.

    Fields:
    - id: Primary key (UUID).
    - username: Unique name for the user.
    - email: Unique email address.
    - password_hash: Stores the hashed password securely.
    - role: Defines the user's role (e.g., 'user', 'admin', 'manager').
    - is_active: Indicates if the user's account is active.
    """

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        """
        Hashes and securely stores the user's password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verifies if a given password matches the stored hash.
        """
        return check_password_hash(self.password_hash, password)


class TokenBlocklist(db.Model):
    """
    Tracks revoked or expired JWT tokens to prevent reuse.

    Fields:
    - id: Primary key (UUID).
    - jti: Unique identifier for the token.
    - created_at: Timestamp when the token was added to the blocklist.
    - expires_at: Expiry timestamp for the token.
    """

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    jti = db.Column(db.String(36), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    expires_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc) + timedelta(days=1))


class Product(db.Model):
    """
    Represents products in the inventory with attributes for identification, categorization, and availability.

    Fields:
    - id: Primary key (UUID).
    - name: Name of the product.
    - description: Detailed description of the product.
    - price: Cost of the product.
    - quantity: Number of items available in stock.
    - category: Classification of the product.
    - deleted_at: Timestamp for soft-deletion; null if active.
    """

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def soft_delete(self):
        """
        Marks the product as deleted by adding a timestamp, without removing it from the database.
        """
        self.deleted_at = datetime.now(timezone.utc)
