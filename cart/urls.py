from .views import cart_add, cart_details, cart_remove
from django.urls import path

urlpatterns = [
    path("", cart_details, name="cart_details"),
    path("add/<int:product_id>/", cart_add, name="cart_add"),
    path("remove/<int:product_id>/", cart_remove, name="cart_remove")
]
