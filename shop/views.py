from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from cart.forms import CartAddProductForm
from shop.models import Category, Produit


def index(request):
    products = Produit.objects.all()
    context = {"title":"bienvenue chez vous","products":products}
    return render(request, "index.html",context )


class ProductList(ListView):
    # model = Produit
    # context_object_name = 'products'
    template_name='shop/produit_list.html'
    
    def get(self, request):
        products = Produit.objects.all()
        categories =Category.objects.all()
        q = request.GET.get("q")
        if q:
            products = Produit.objects.filter(
                Q(name__icontains=q) |
                Q(desciption__icontains=q) |
                Q(category__name__icontains=q)
                )
        return render(request, self.template_name, {"products":products, "categories":categories})
    
class ProductDetail(DetailView):
    model = Produit
    context_object_name = 'product'
    template_name='shop/product_details.html'
    
    # def get(self, request):
    #     return render(request, self.template_name, {"product": product})
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["cart_product_form"] = CartAddProductForm()
        return context
