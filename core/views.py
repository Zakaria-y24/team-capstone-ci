from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Cart, CartItem, Product
from core.forms import ProductForm, UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

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

def cart(request):
    context = {
        'cart_items': [], # Replace with cart items
        'total_price': 0, # Replace with calculated total
    }
    return render(request, 'cart.html', context)

@login_required
def account_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('account')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'account.html', {
        'form': form,
        'user_data': request.user
    })

def cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key or request.session.save()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)

    cart_items = cart.items.select_related('product')
    total_price = sum(item.subtotal() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Get or create cart (user or session-based)
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.save()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)

    # Check if item already in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('products')

def update_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart = Cart.objects.filter(session_key=request.session.session_key).first()

    if not cart:
        return redirect('cart')

    for item in cart.items.all():
        quantity = request.POST.get(f'quantity_{item.id}')
        if quantity and quantity.isdigit():
            item.quantity = max(1, int(quantity))
            item.save()

    return redirect('cart')


def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id)
        item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart')


def checkout(request):
    return render(request, 'checkout.html') 