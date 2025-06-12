from django.shortcuts import render

from core.models import Product

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})