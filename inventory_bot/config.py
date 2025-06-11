import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "DISCORD_BOT_TOKEN": os.getenv("DISCORD_BOT_TOKEN"),
        "SERPAPI_KEY": os.getenv("SERPAPI_KEY")
    }
