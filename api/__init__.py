from flask import Flask


def create_app(config: str = "config.DevConfig"):
    """Factory for the core application instance."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    with app.app_context():
        from api.psql.utils import db_setup

        from . import routes  # noqa: F401

        db_setup()

        return app
