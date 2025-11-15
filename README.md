# Portable Flask Application

A production-ready Flask application with modern Python tooling, UV package management, and containerization.

##  Project Structure

```
portable-flask/
├── app/                    # Application code
│   ├── __init__.py        # App factory
│   └── routes.py          # Route definitions
├── config/                 # Configuration
│   ├── __init__.py
│   └── settings.py        # Environment configs
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_routes.py     # Route tests
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # CI/CD pipeline
├── Dockerfile             # Multi-stage Docker build
├── pyproject.toml         # Project dependencies (UV)
├── wsgi.py               # WSGI entry point
└── README.md
```

##  Quick Start

### Prerequisites

- Python 3.12+
- [UV](https://github.com/astral-sh/uv) package manager
- Docker (optional, for containerization)

### Local Development

1. **Install UV** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Install dependencies**:
```bash
uv pip install -r pyproject.toml
uv pip install -e ".[dev]"
```

3. **Run the application**:
```bash
# Development mode
FLASK_ENV=development python wsgi.py

# Or with Flask's built-in server
FLASK_APP=wsgi:app flask run --host=0.0.0.0 --port=8080
```

4. **Run tests**:
```bash
pytest
```

5. **Code quality checks**:
```bash
# Format code
black app config tests

# Lint
flake8 app config

# Type checking
mypy app config
```

## 🐳 Docker

### Build and run with Docker

```bash
# Build the image
docker build -t portable-flask .

# Run the container
docker run -p 8080:8080 portable-flask

# Run detached
docker run -d -p 8080:8080 portable-flask
```

### Using GitHub Container Registry

```bash
# Pull the latest image
docker pull ghcr.io/kelleyblackmore/portable-flask:latest

# Run the container
docker run -p 8080:8080 ghcr.io/kelleyblackmore/portable-flask:latest
```

##  API Endpoints

- `GET /` - Hello World
- `GET /health` - Health check endpoint (returns status and hostname)
- `GET /info` - Application info (version, environment)

##  Configuration

The application supports multiple environments through configuration classes:

- `development` - Debug mode enabled
- `production` - Production settings
- `testing` - Testing configuration

Set the environment using the `FLASK_ENV` variable:
```bash
export FLASK_ENV=production
```

### Environment Variables

- `FLASK_ENV` - Application environment (development/production/testing)
- `SECRET_KEY` - Secret key for Flask (required in production)

## 🧪 Testing

Run the test suite with coverage:
```bash
pytest --cov=app --cov-report=html
```

##  Deployment

The application uses Gunicorn as the WSGI server in production. The Dockerfile is configured with:

- Multi-stage builds for smaller images
- Non-root user for security
- Health checks
- 4 workers with 2 threads each
- Optimized for production use

##  CI/CD

GitHub Actions automatically:
- Runs tests on push/PR
- Performs code quality checks (flake8, black, mypy)
- Builds and pushes Docker images to GHCR on main branch

##  Development Workflow

1. Create a new branch for your feature
2. Make changes and ensure tests pass
3. Run code quality checks
4. Push and create a PR
5. CI/CD will run automatically
6. Merge after approval

##  Technologies

- **Flask 3.0+** - Web framework
- **UV** - Fast Python package manager
- **Gunicorn** - WSGI HTTP server
- **Docker** - Containerization
- **pytest** - Testing framework
- **black** - Code formatter
- **flake8** - Linter
- **mypy** - Type checker

##  License

This project is open source and available under the MIT License.

