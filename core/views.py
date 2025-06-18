from django.core.paginator import Paginator
from django.shortcuts import render
from core.models import Product

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def products(request):
    category = request.GET.get('category')
    product_list = Product.objects.all()

    if category:
        product_list = product_list.filter(category=category)

    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {
        'page_obj': page_obj,
        'category': category,
    })