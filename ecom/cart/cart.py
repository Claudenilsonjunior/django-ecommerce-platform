
class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #Get the current session key
        cart = self.session.get('session_key')
        
        
        #If the session key is not set, create a new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # cart is available on all pages of the site
        self.cart = cart
        
    def add_to_cart(self, product):
        product.id = str(product.id)
        
        if product.id in self.cart:
            pass
        else: 
            self.cart[product.id] = {'price': str(product.price)}
        
        self.session.modified = True