from django.http import HttpResponse, HttpResponseRedirect
import paydunya
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from paydunya import InvoiceItem, Store, Invoice

from orders.models import Order
from send_mail.views import payment_successfull_email

paydunya.debug = True
paydunya.api_keys = settings.PAYDUNYA_ACCESS_TOKENS

store = Store(name='Magasin Chez Jaba')


def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, pk=order_id)
    order_items = order.items.all()
    items = [
    InvoiceItem(
        name=item.produit.name,
        quantity=item.quantity,
        unit_price=str(item.price),
        total_price=str(item.price * item.quantity),
        description=item.produit.name
    ) for item in order_items]
    invoice = paydunya.Invoice(store)
    # host = request.get_host()
    # invoice.callback_url =  f"http://{host}/payment-done",
    # invoice.cancel_url = f"http://{host}/payment-canceled",
    # invoice.return_url = f"http://{host}/payment-done",
    
    invoice.add_items(items)
    successful, response = invoice.create()
    if successful:
        return redirect(response.get("response_text"))
        
        
    
    
# def payment_done(request):
#     token = request.GET.get("token")
#     invoice = Invoice()
#     successful = invoice.confirm(token)
#     if successful:
#         return HttpResponse("<h2>Merci pour le paiment</h2>")

# def payment_canceled(request):
#     return HttpResponse("<h2>Vous avez annule le paiement</h2>")