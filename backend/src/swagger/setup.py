from flask_swagger_ui import get_swaggerui_blueprint


def register_swagger_api(app):
    """
    Sets up Swagger API documentation for the application.
    """
    swaggerui_blueprint = get_swaggerui_blueprint(
        app.config.get("SWAGGER_URL"),
        app.config.get("API_URL"),
        config={'app_name': app.config.get("APP_NAME")}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=app.config.get("SWAGGER_URL"))
