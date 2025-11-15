"""Initialize the Flask application with configuration."""
from flask import Flask
from config.settings import config
import os


def create_app(config_name: str = "default") -> Flask:
    """Application factory pattern."""
    app = Flask(__name__)

    # Load configuration
    config_name = os.environ.get("FLASK_ENV", config_name)
    app.config.from_object(config[config_name])

    # Register blueprints
    from app.routes import main_bp

    app.register_blueprint(main_bp)

    return app
