import os
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

def get_env(var_name: str, default=None):
    """
    Retrieve an environment variable, with optional default fallback.
    Raises an error if not found and no default is provided.
    """
    value = os.getenv(var_name)
    if value is not None:
        return value
    if default is not None:
        return default
    raise EnvironmentError(f"Environment variable '{var_name}' is not set.")
