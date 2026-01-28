# External Imports
import os


# Get the EIA API key from environment variables
EIA_API_KEY : str | None = os.getenv("EIA_API_KEY", None)

# If None raise an error
if not EIA_API_KEY:
    raise RuntimeError("Cannot find EIA API Key in Environment Variables")
