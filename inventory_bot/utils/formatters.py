
import discord

def format_inventory_embed(data, sku, zip_code, retailer, radius):
    embed = discord.Embed(
        title=f"{retailer} Inventory for '{sku}'",
        description=f"ZIP: {zip_code} | Radius: {radius}mi",
        color=0x00aaff
    )
    for store in data.get("stores", []):
        embed.add_field(
            name=store["location"],
            value=f"Stock: {store['stock']} | Price: {store['price']}",
            inline=False
        )
    embed.set_footer(text="Mock data. Live data integration pending.")
    return embed
