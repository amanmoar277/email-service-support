"""Registering blueprints(or register routes).
"""

def attach_route_via_blueprint(app):
    """Registering API Blueprints.
    """

    from src.routes.site_wide import api_default_blueprint
    from src.routes.data import api_data_blueprint
    from src.routes.email import api_email_blueprint
    app.register_blueprint(api_data_blueprint, url_prefix='/api/data')
    app.register_blueprint(api_email_blueprint, url_prefix='/api/email')
    app.register_blueprint(api_default_blueprint)
