from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from .models import Product

def product_list(request):
    products = Product.objects.all()   # fetch all products
    return render(request, "products/products_list.html", {"products": products})


def home(request):
    return render(request, "products/home.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:add_category")
    else:
        form = CategoryForm()
    return render(request, "products/category_form.html", {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products:add_product")
    else:
        form = ProductForm()
    return render(request, "products/product_form.html", {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {'categories': categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/products_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})
