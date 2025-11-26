from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    items = Product.objects.all()
    return render(request, 'products/list.html', {"items": items})

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/add.html', {"form": form})
