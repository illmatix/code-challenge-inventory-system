from src.models import TokenBlocklist


def register_jwt_handlers(jwt):
    """
    Register JWT handlers, such as token revocation checks.

    Args:
        jwt: The Flask-JWT-Extended instance.
    """

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        """
        Check if the provided token is revoked by looking up its JTI in the TokenBlocklist.

        Args:
            jwt_header (dict): The JWT header data.
            jwt_payload (dict): The JWT payload data.

        Returns:
            bool: True if the token is revoked, False otherwise.
        """
        jti = jwt_payload["jti"]
        token = TokenBlocklist.query.filter_by(jti=jti).first()
        return token is not None
