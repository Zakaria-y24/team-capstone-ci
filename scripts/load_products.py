import os
import sys
import django
from django.core.files import File

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from core.models import Product

# Wipe existing products (optional)
Product.objects.all().delete()

# Product data (with categories)
product_data = [
    {
        "name": "Daisy Dome",
        "description": "A preserved dome of white daisies in a resin block.",
        "price": 19.99,
        "filename": "Daisy_Dome.jpg",
        "category": "flowers"
    },
    {
        "name": "Lavender Glow Pendant",
        "description": "Lavender stems in a soft violet translucent resin pendant.",
        "price": 18.99,
        "filename": "diy-flower-pendant-1-54.jpg.webp",
        "category": "flowers"
    },
    {
        "name": "Hydrangea Bloom",
        "description": "Vibrant blue hydrangea petals captured in resin.",
        "price": 22.99,
        "filename": "hydrandea.webp",
        "category": "flowers"
    },
    {
        "name": "Maple Leaf Resin",
        "description": "Autumn maple leaves embedded in amber-toned resin.",
        "price": 24.99,
        "filename": "maple_leaf_resin.jpg",
        "category": "leaves"
    },
    {
        "name": "Pinecone Drop",
        "description": "Mini pinecones encased in clear resin for a natural look.",
        "price": 16.99,
        "filename": "pinecone.jfif",
        "category": "leaves"
    },
    {
        "name": "Rose Bloom Cube",
        "description": "A preserved red rose encased in a crystal-clear resin cube.",
        "price": 25.99,
        "filename": "Rose_Bloom_Cube.jfif",
        "category": "flowers"
    },
    {
        "name": "Sunflower Mini Block",
        "description": "Mini sunflowers in a compact block of clear resin.",
        "price": 21.99,
        "filename": "Sunflower_Mini_Block.jpg",
        "category": "seasonal"
    },
    {
        "name": "Wild Flower Resin",
        "description": "A mix of wildflowers captured in a vivid resin piece.",
        "price": 23.99,
        "filename": "Wild_flower_resin.jpg",
        "category": "flowers"
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
            category=item["category"]
        )
        product.image.name = f"product_images/{item['filename']}"
        product.save()
        print(f"Created: {item['name']}")
