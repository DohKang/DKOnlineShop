from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse
# Create your views here.

#get session id
def get_session_id(request):
    session = request.session.session_key
    if not session:
        session = request.session.create()
    return session


def add_cart(request, product_id):
    #get prodcut
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=get_session_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = get_session_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
    return HttpResponse(cart_item.product)
    exit()
    return redirect('cart')



def cart(request):
    return render(request, 'store/cart.html')