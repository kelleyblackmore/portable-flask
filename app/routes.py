"""Main routes for the application."""

from flask import Blueprint, jsonify
import socket
import os

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def hello() -> str:
    """Return a simple greeting."""
    return "Hello World!"


@main_bp.route("/health")
def health() -> tuple[dict[str, str], int]:
    """Health check endpoint."""
    return jsonify({"status": "healthy", "hostname": socket.gethostname()}), 200


@main_bp.route("/info")
def info() -> tuple[dict[str, str], int]:
    """Return application information."""
    return (
        jsonify(
            {
                "app": "portable-flask",
                "version": "0.1.0",
                "environment": os.environ.get("FLASK_ENV", "development"),
            }
        ),
        200,
    )
