import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from .config import get_config
from .utils.logger import setup_logger
from .commands.inventory import setup_inventory_command

load_dotenv()
config = get_config()
logger = setup_logger()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    try:
        await setup_inventory_command(bot)
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} global commands.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.event
async def on_disconnect():
    logger.warning("Bot disconnected from Discord.")

bot.run(config["DISCORD_BOT_TOKEN"])
