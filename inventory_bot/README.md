
# Discord Inventory Bot

A Discord bot that checks product inventory by SKU and ZIP across major retailers.

## Features
- `/inventory` - Lookup stock and pricing
- `/retailers` - Show supported stores
- `/ping` - Test bot health
- Logging + embedded responses

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add a `.env` file:
```
DISCORD_BOT_TOKEN=your_token_here
DEFAULT_RADIUS=10
```

3. Run:
```bash
python bot.py
```

## TODO
- Add real inventory fetching logic to services/*.py
- Deploy using Render or Railway
