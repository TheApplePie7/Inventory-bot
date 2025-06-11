import discord
from discord import app_commands
from discord.ext import commands
from inventory_bot.services import walmart

async def setup_inventory_command(bot: commands.Bot):
    @bot.tree.command(name="inventory", description="Check inventory for a product")
    @app_commands.describe(
        sku="Walmart SKU to check",
        zip_code="ZIP code to search around",
        radius="Radius in miles (optional, default 25)"
    )
    async def inventory(interaction: discord.Interaction, sku: str, zip_code: str, radius: int = 25):
        await interaction.response.defer(thinking=True)

        try:
            data = await walmart.scrape_walmart_inventory(sku, zip_code, radius)
        except Exception as e:
            await interaction.followup.send(f"❌ Error during inventory fetch: {e}")
            return

        embed = discord.Embed(
            title=f"Walmart Inventory for SKU: {sku}",
            description=f"ZIP: {zip_code} | Radius: {radius}mi",
            color=discord.Color.blue()
        )

        if data.get("stores"):
            for store in data["stores"]:
                embed.add_field(
                    name=store.get("location", "Unknown"),
                    value=f"Stock: {store.get('stock', 'Unknown')} | Price: {store.get('price', 'N/A')}",
                    inline=False
                )
        else:
            embed.add_field(name="Walmart", value="Stock: Unknown | Price: N/A\n⚠️ Data may be incomplete.")

        await interaction.followup.send(embed=embed)

async def setup_ping_command(bot: commands.Bot):
    @bot.tree.command(name="ping", description="Check bot latency")
    async def ping(interaction: discord.Interaction):
        latency = round(bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! Latency is {latency}ms")
