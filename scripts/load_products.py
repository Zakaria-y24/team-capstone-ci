import os
import sys
import django
from django.core.files import File

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from core.models import CartItem, Product

# Wipe existing products and cart items (optional)
CartItem.objects.all().delete()

Product.objects.all().delete()

# Product data (with categories)
product_data = [
    {
        "name": "Botanical Glow Tea Light Holder",
        "description": "Elegant resin candle holder featuring real dried greenery—perfect for adding a natural, calming glow to any setting.",
        "price": 20.00,
        "filename": "BotanicalGlowTeaLightHolder.webp",
        "category": "Leaves",
        "stock": 5
    },
    {
        "name": "Four Leaf Clover",
        "description": "A charming resin mini block featuring a four-leaf clover—perfect for a touch of natural luck and simplicity.",
        "price": 15.00,
        "filename": "FourLeafClover.webp",
        "category": "Leaves",
        "stock": 5
    },
    {
        "name": "Leaf Forest Series",
        "description": "A striking resin piece featuring layered forest leaves, evoking the calm and depth of a quiet woodland.",
        "price": 28.00,
        "filename": "LeafForestSeries.jpg",
        "category": "Leaves",
        "stock": 0
    },
    {
        "name": "Emerald Leaf Resin Block",
        "description": "A serene green resin block featuring delicate pressed leaves over a swirling emerald backdrop—simple and nature-inspired.",
        "price": 21.00,
        "filename": "EmeraldLeafBlock.webp",
        "category": "Leaves",
        "stock": 5
    },
    {
        "name": "Coastal Christmas Ornament",
        "description": "Aqua Christmas Tree with shells and Beach, Beachy Christmas, Resin ornament, Handmade",
        "price": 16.00,
        "filename": "CoastalChristmasOrnament.webp",
        "category": "Seasonal",
        "stock": 5
    },
    {
        "name": "Blush Garden Resin Slice",
        "description": "A romantic half-moon resin block showcasing preserved blush roses and ivory blooms, perfect for timeless floral décor.",
        "price": 49.00,
        "filename": "BlushGardenResinSlice.jpg",
        "category": "Flowers",
        "stock": 5
    },
    {
        "name": "Gold Flake Autumn Leaves Coaster",
        "description": "A handcrafted resin coaster featuring delicate autumn leaves and shimmering gold flakes, evoking the warmth of fall.",
        "price": 22.00,
        "filename": "GoldFlakeAutumnLeavesCoaster.webp",
        "category": "Seasonal",
        "stock": 5
    },
    {
        "name": "Ocean Breeze Shell Pyramid",
        "description": "A coastal-inspired resin pyramid filled with seashells and ocean-blue hues, bringing seaside serenity to any space.",
        "price": 31.00,
        "filename": "OceanBreezeShellPyramid.jpg",
        "category": "Miscellaneous",
        "stock": 5
    },
    {
        "name": "Golden Fern Sunset Panel",
        "description": "Gold fern dried plant with Wooden arch frame.",
        "price": 34.00,
        "filename": "GoldenFernSunsetPanel.webp",
        "category": "Leaves",
        "stock": 5
    },
    {
        "name": "Lavender Bloom Crystal Tray",
        "description": "A handcrafted resin tray featuring real lavender blooms and crystal accents for a calming, elegant touch.",
        "price": 29.00,
        "filename": "LavenderBloomCrystalTray.jpg",
        "category": "Miscellaneous",
        "stock": 5
    },
    {
        "name": "Daisy Dome LED Square Block",
        "description": "Daisy Dome LED Block with real pressed flowers and soft LED lights—simple, modern, and elegant.",
        "price": 32.00,
        "filename": "Daisy_Dome_LED.png",
        "category": "Flowers",
        "stock": 5
    },
]

# Correct path to media/product_images
MEDIA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media", "product_images")

# Create products
for item in product_data:
    image_path = os.path.join(MEDIA_PATH, item["filename"])
    if not os.path.exists(image_path):
        print(f"File not found: {item['filename']}")
        continue

    with open(image_path, "rb") as img_file:
        product = Product(
            name=item["name"],
            description=item["description"],
            price=item["price"],
            category=item["category"],
            stock=item["stock"] 
        )
        product.image.name = f"product_images/{item['filename']}"
        product.save()
        print(f"Created: {item['name']}")
