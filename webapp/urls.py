from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static
from core.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about_us, name='about_us'),  # Use the correct view name
    path('manage/', views.admin_dashboard, name='admin_dashboard'),
    path('manage/products/', views.admin_product_list, name='admin_product_list'),
    path('manage/products/add/', views.admin_product_create, name='admin_product_create'),
    path('manage/products/edit/<int:pk>/', views.admin_product_update, name='admin_product_update'),
    path('manage/products/delete/<int:pk>/', views.admin_product_delete, name='admin_product_delete'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('cart/', views.cart, name='cart'),
    path('account/', views.account_view, name='account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
