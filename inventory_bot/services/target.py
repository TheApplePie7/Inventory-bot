
def get_target_inventory(sku, zip_code, radius):
    return {
        "stores": [
            {"location": "Target - City Center", "stock": "Out of Stock", "price": "$34.99"},
        ],
        "radius": radius
    }
