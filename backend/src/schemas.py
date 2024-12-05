from marshmallow import Schema, fields, validate

# Schema for validating and serializing User data.
# Ensures data integrity for user-related operations, including registration and updates.
class UserSchema(Schema):
    # UUID for the user; read-only and auto-generated.
    id = fields.Str(dump_only=True)

    # Username must be provided, with a length constraint between 3 and 80 characters.
    username = fields.Str(
        required=True,
        validate=validate.Length(
            min=3,
            max=80,
            error="Username must be between 3 and 80 characters long"
        ),
        error_messages={"required": "Username is required"}
    )

    # Email is required and must conform to a valid email format.
    email = fields.Email(
        required=True,
        validate=validate.Email(),
        error_messages={
            "required": "Email is required",
            "invalid": "Invalid email address"
        }
    )

    # Password is write-only and must meet the length requirements for security.
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(
            min=6,
            max=200,
            error="Password must be between 6 and 200 characters long"
        ),
        error_messages={"required": "Password is required"}
    )

    # Role indicates the user's permission level; defaults to "user".
    role = fields.Str(
        validate=validate.OneOf(
            ["user", "admin", "manager"],
            error="Role must be one of: user, admin, manager"
        ),
        missing="user"
    )

    # Active status determines whether the user can access the system; defaults to True.
    is_active = fields.Bool(missing=True)


# Schema for validating Login data.
# Ensures username and password are provided during login attempts.
class LoginSchema(Schema):
    # Username is mandatory for login.
    username = fields.Str(
        required=True,
        error_messages={"required": "Username is required for login"}
    )

    # Password is mandatory for login.
    password = fields.Str(
        required=True,
        error_messages={"required": "Password is required for login"}
    )


# Schema for validating and serializing Product data.
# Used for ensuring valid product details in inventory management.
class ProductSchema(Schema):
    # UUID for the product; read-only and auto-generated.
    id = fields.Str(dump_only=True)

    # Product name must be provided, with a length constraint between 1 and 100 characters.
    name = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=100,
            error="Product name must be between 1 and 100 characters long"
        ),
        error_messages={"required": "Product name is required"}
    )

    # Description of the product must be provided, with a length constraint between 1 and 255 characters.
    description = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=255,
            error="Description must be between 1 and 255 characters long"
        ),
        error_messages={"required": "Product description is required"}
    )

    # Price must be a non-negative number and is required.
    price = fields.Float(
        required=True,
        validate=validate.Range(
            min=0,
            error="Price must be a non-negative number"
        ),
        error_messages={"required": "Product price is required"}
    )

    # Quantity must be a non-negative integer and is required.
    quantity = fields.Int(
        required=True,
        validate=validate.Range(
            min=0,
            error="Quantity must be a non-negative integer"
        ),
        error_messages={"required": "Product quantity is required"}
    )

    # Category name must be provided, with a length constraint between 1 and 50 characters.
    category = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=50,
            error="Category must be between 1 and 50 characters long"
        ),
        error_messages={"required": "Product category is required"}
    )
