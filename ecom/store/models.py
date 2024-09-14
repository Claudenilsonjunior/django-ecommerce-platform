from django.db import models
import datetime

class Category(models.Model):

    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(default = '')
    price = models.DecimalField(default = 0, max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
    image = models.ImageField(upload_to='uploads/products')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self): 
        return self.name

class Order(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.product.name} ordered by {self.customer.first_name} {self.customer.last_name}'
