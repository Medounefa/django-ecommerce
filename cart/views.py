from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm

from .models import Cart
from shop.models import Produit

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produit, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product=product, quantity=cleaned_data["quantity"], override_quantity=cleaned_data["override"])
        return redirect("cart_details")
    

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product= get_object_or_404(Produit, id = product_id)
    cart.remove(product)
    
    return redirect("cart_details")


def cart_details(request):
    cart =Cart(request)
    for item in cart :
        item['update_quantity_form'] = CartAddProductForm(initial={"quantity":item["quantity"], "override":True})
    return render(request, "cart/cart_details.html",{"cart":cart})