import json
from pathlib import Path

CONFIG_PATH = Path(".tableau_config.json")

# Default fallback config (optional)
DEFAULT_CONFIG = {
    "TABLEAU_SERVER_URL": "https://your-tableau-server.com",
    "TABLEAU_SITE_ID": "your-site-id",
    "TABLEAU_PERSONAL_ACCESS_TOKEN_NAME": "your-pat-name",
    "TABLEAU_PERSONAL_ACCESS_TOKEN_SECRET": "your-pat-secret",
    "OPENAI_API_KEY": "your-openai-api-key"
}

# ----------------------------------------
# 📖 Load current config from JSON
# ----------------------------------------
def load_config():
    """Load config from .tableau_config.json, or use default if missing/broken."""
    if not CONFIG_PATH.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

def save_config(data: dict):
    """Save config dictionary to the config file."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_config_value(key: str, default=None):
    """Get a specific config value by key."""
    config = load_config()
    return config.get(key, default)