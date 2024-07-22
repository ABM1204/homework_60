"""
URL configuration for HW60 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from online_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.CategoryListView.as_view(), name='categories_view'),
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add_view'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit_view'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete_category_view'),

    path('', views.ProductListView.as_view(), name='products_view'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_view'),
    path('product/add/', views.ProductCreateView.as_view(), name='product_add_view'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit_view'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_product_view'),

    path('product/add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart')
]
