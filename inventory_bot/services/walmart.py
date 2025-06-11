import logging
import requests

logger = logging.getLogger(__name__)

class WalmartProduct:
    def __init__(self, data: dict):
        self.data = data

    def extract_inventory_info(self) -> dict:
        product = self.data.get("product_result", {})
        price = product.get("price_map", {}).get("price")
        in_stock = product.get("in_stock", False)

        pickup_available = any(
            pickup.get("availability") == "AVAILABLE"
            for pickup in product.get("pickup_options", [])
        )

        stock_status = "In Stock" if in_stock or pickup_available else "Out of Stock"

        return {
            "title": product.get("title"),
            "stock": stock_status,
            "price": price,
            "url": product.get("product_page_url")
        }

class WalmartSearch:
    BASE_URL = "https://serpapi.com/search"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search_product(self, sku: str, zip_code: str, radius: int = 25):
        params = {
            "engine": "walmart_product",
            "product_id": sku,
            "store_zip": zip_code,
            "device": "desktop",
            "hl": "en",
            "output": "json",
            "source": "python",
            "api_key": self.api_key
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching Walmart product data: {e}")
            return None
import logging
from .serpapi import fetch_product_data  # adjust if you use another fetch method

logger = logging.getLogger(__name__)

def scrape_walmart_inventory(sku: str, zip_code: str, radius: int = 25) -> dict:
    logger.info(f"🔍 Using SerpAPI to fetch data for SKU: {sku}, ZIP: {zip_code}, Radius: {radius}mi")
    data = fetch_product_data(sku, zip_code, radius)
    logger.debug("📦 Full SerpAPI results:\n%s", data)

    if not data:
        logger.warning("⚠️ No data returned from SerpAPI")
        return {
            "title": "Unknown Product",
            "stock": "Unknown",
            "price": None,
            "url": None
        }

    return extract_inventory_info(data)
