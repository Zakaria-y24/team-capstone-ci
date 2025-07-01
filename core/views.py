from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Cart, CartItem, Product
from core.forms import ProductForm, UserRegistrationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Public views
def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def about_us(request):
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

# Admin check helper
def is_admin(user):
    return user.is_staff

# Admin views
@user_passes_test(is_admin)
def admin_product_list(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'admin/product_list.html', {'products': products})

@user_passes_test(is_admin)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'admin/product_form.html', {'form': form, 'action': 'Add'})

@user_passes_test(is_admin)
def admin_product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin/product_form.html', {'form': form, 'action': 'Edit'})

@user_passes_test(is_admin)
def admin_product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_product_list')
    return render(request, 'admin/product_confirm_delete.html', {'product': product})

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

# Registration and logout
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

def custom_logout(request):
    logout(request)
    return redirect('home')



