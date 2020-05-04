from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductForm

# Create your views here.
@login_required
def products_list(request):
    products = Products.objects.all()
    return render(request, 'product.html', {'products' : products})


@login_required
def products_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('products_list')
    return render(request, 'product_form.html', {'form' : form})


@login_required
def products_update(request, id):
    product = get_object_or_404(Products, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('products_list')

    return render(request, 'product_form.html', {'form' : form})


@login_required
def products_delete(request, id):
    product = get_object_or_404(Products, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    
    return render(request, 'delete_confirm.html', {'product' : product})