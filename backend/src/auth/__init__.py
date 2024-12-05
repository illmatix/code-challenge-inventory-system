from .jwt_handlers import register_jwt_handlers

def register_auth(jwt):
    register_jwt_handlers(jwt)