from django.contrib import admin
from django.urls import path

from core import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('manage/', views.admin_dashboard, name='admin_dashboard'), # New Dashboard URL
    path('manage/products/', views.admin_product_list, name='admin_product_list'),
    path('manage/products/add/', views.admin_product_create, name='admin_product_create'),
    path('manage/products/edit/<int:pk>/', views.admin_product_update, name='admin_product_update'),
    path('manage/products/delete/<int:pk>/', views.admin_product_delete, name='admin_product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)