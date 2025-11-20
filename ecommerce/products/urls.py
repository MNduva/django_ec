from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.home, name="home"),
    path('categories/', views.category_list, name="category_list"),
    path('products/', views.product_list, name="product_list"),
    path('add-category/', views.add_category, name="add_category"),
    path('add-product/', views.add_product, name="add_product"),
    path('products/<int:pk>/', views.product_detail, name="product_detail"),
]
