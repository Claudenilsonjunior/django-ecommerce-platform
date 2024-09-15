from .cart import Cart

# Create context processor
def cart(request):
    #Return the default data from our cart
    return {'cart': Cart(request)}