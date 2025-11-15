"""Tests for the main routes."""

import pytest
from app import create_app


@pytest.fixture
def app():
    """Create and configure a test app instance."""
    app = create_app("testing")
    yield app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


def test_hello(client):
    """Test the hello endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello World!" in response.data


def test_health(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "hostname" in data


def test_info(client):
    """Test the info endpoint."""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["app"] == "portable-flask"
    assert data["version"] == "0.1.0"
    assert "environment" in data
