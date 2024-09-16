from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'cart_summary.html', {"cart_products": cart_products})

def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        
        #Getting the Id of the product
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart.add_to_cart(product = product)
        
        #Getting cart quantity
        
        cart_quantity = cart.__len__()
        
        #response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'Quantity': cart_quantity})
        return response

def delete_from_cart(request):
    pass

def update_cart(request): 
    pass