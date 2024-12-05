from flask import Blueprint, send_from_directory, current_app



def register_routes(app):
    from src.routes.products import products
    from src.routes.auth import auth
    from src.routes.users import users

    app.register_blueprint(products, url_prefix='/api/products')
    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(users, url_prefix='/api/users')

    # Serve Swagger.yaml
    @app.route("/swagger.yaml")
    def serve_swagger_yaml():
        return send_from_directory("../public", "swagger.yaml")

    # Serve Swagger UI (Optional: If you use a local Swagger UI setup)
    @app.route("/swagger-ui/<path:path>")
    def serve_swagger_ui(path):
        return send_from_directory("../public/swagger-ui", path)