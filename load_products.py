import os
import django
from django.core.files import File

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from core.models import Product

# Product data
product_data = [
    {
        "name": "Daisy Dome",
        "description": "A preserved dome of white daisies in a resin block.",
        "price": 19.99,
        "filename": "Daisy Dome.jpg"
    },
    {
        "name": "Lavender Glow Pendant",
        "description": "Lavender stems in a soft violet translucent resin pendant.",
        "price": 18.99,
        "filename": "diy-flower-pendant-1-54.jpg.webp"
    },
    {
        "name": "Hydrangea Bloom",
        "description": "Vibrant blue hydrangea petals captured in resin.",
        "price": 22.99,
        "filename": "hydrandea.webp"
    },
    {
        "name": "Maple Leaf Resin",
        "description": "Autumn maple leaves embedded in amber-toned resin.",
        "price": 24.99,
        "filename": "maple leaf resin.jpg"
    },
    {
        "name": "Pinecone Drop",
        "description": "Mini pinecones encased in clear resin for a natural look.",
        "price": 16.99,
        "filename": "pinecone.jfif"
    },
    {
        "name": "Rose Bloom Cube",
        "description": "A preserved red rose encased in a crystal-clear resin cube.",
        "price": 25.99,
        "filename": "Rose Bloom Cube.jfif"
    },
    {
        "name": "Sunflower Mini Block",
        "description": "Mini sunflowers in a compact block of clear resin.",
        "price": 21.99,
        "filename": "Sunflower Mini Block.jpg"
    },
    {
        "name": "Wild Flower Resin",
        "description": "A mix of wildflowers captured in a vivid resin piece.",
        "price": 23.99,
        "filename": "Wild flower resin.jpg"
    },
]

# Path to media directory
MEDIA_PATH = os.path.join("media", "products")

# Create each product
for item in product_data:
    image_path = os.path.join(MEDIA_PATH, item["filename"])
    if not os.path.exists(image_path):
        print(f"File not found: {item['filename']}")
        continue

    with open(image_path, "rb") as img_file:
        product = Product(
            name=item["name"],
            description=item["description"],
            price=item["price"]
        )
        product.image.save(item["filename"], File(img_file), save=True)
        print(f"Created: {item['name']}")
