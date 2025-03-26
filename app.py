import os
from autogenstudio.web.api import create_app

# Create the FastAPI app
app = create_app()

# Configure database URI from environment variables
if "POSTGRES_CONNECTION_STRING" in os.environ:
    # Format the connection string for SQLAlchemy
    conn_str = os.environ["POSTGRES_CONNECTION_STRING"]
    database_uri = f"postgresql+psycopg://{conn_str}"
else:
    # Default to SQLite if no PostgreSQL connection string is provided
    database_uri = "sqlite:///database.sqlite"

# Set the app directory
app_dir = os.environ.get("APP_DIR", ".autogenstudio")
os.makedirs(app_dir, exist_ok=True)