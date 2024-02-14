from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from cart.models import Cart
from orders.models import OrderItem
from send_mail.views import send_new_order_email, send_new_order_email_with_template
from .forms import OrdersCreateForm
# from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    
    if request.method == "POST":
        form = OrdersCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            email = form.cleaned_data.get("email")
            for item in cart :
                OrderItem.objects.create(
                    order=order,
                    produit = item["product"],
                    price = item["price"],
                    quantity = item["quantity"]
                )
            cart.clear()
            request.session["order_id"] = order.id
            
            #envoi un mail au client
            # send_mail(
            #     "Votre commande sur Jaba",
            #     "Nous avons bien recu votre commande.",
            #     "contact@jaba.com",
            #     [email],
            #     fail_silently=False,
            # )
            # send_new_order_email(email)
            send_new_order_email_with_template(email)
            return redirect("payment-process")
    
    else : 
        form = OrdersCreateForm()
    return render(request, "orders/create.html", {"cart": cart, "form": form}, )

def order_created(request):
    return render(request, "orders/created.html")