# from django.db import models
# from django.conf import settings
# from shop.models import Produit
# from decimal import Decimal

# # Create your models here.

# class Cart(object):
#     def __init__(self, request):
#         """
#         initialiser le panier
#         """
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID] ={}
#         self.session = cart
        
#     def save(self):
#       self.session.modified = True
    
#     #ajouter un panier
    
#     def add(self, product, quantity=1, override_quantity=False):
#         product_id = str(product.id)
        
#         if product_id not in self.cart :
#             self.cart[product_id] = {"quantity":0, "price":str(product.id)}
#         if override_quantity :
#             self.cart[product_id]["quantity"] = quantity
#         else :
#             self.cart[product_id]["quantity"] += quantity
#         self.save()
        
#     #supprimer les elements
    
#     def remove(self, product):
#         product_id = str(product.id)
        
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()
    
#     #recuperer les elemenst
    
#     def __iter__(self):
#         product_ids =self.cart.keys()
#         products = Produit.object.filter(id__in=product_ids)
#         for product in products:
#             cart[str(product.id)]["product"] = product
#         cart = self.cart.copy()
        
#         for item in cart.value():
#             item["price"] = Decimal(item["price"]) 
#             item["total_price"] = item["price"] * item["quantity"]
#             yield item
            
#     #compter les elements sur le panier
    
#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())
    
#     def get_total_price(self):
#         return sum(Decimal(item["price"] * item["quantity"]) for item in self.cart.values())
    
    
#     #vider le panier
    
#     def clear(self):
#         del self.session[settings.CART_SESSION_ID]
#         self.save()