from src.models import User
from src.extensions import db
from flask import current_app

def seed_admin():
    """Seeds the admin user into the database using .env values."""
    # Retrieve admin credentials from the app's configuration
    username = current_app.config.get("ADMIN_USER", "default_admin")
    email = current_app.config.get("ADMIN_EMAIL", "admin@example.com")
    password = current_app.config.get("ADMIN_PASS", "defaultpassword")

    # Check if an admin user already exists
    admin_user = User.query.filter_by(username=username).first()
    if not admin_user:
        # Create the admin user
        admin = User(
            username=username,
            email=email,
            role="admin",
            is_active=True,
        )
        # Set the admin user's password
        admin.set_password(password)
        # Add the user to the session and commit
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user '{username}' created successfully.")
    else:
        print(f"Admin user '{username}' already exists.")
