from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.cart_summary, name='cart_summary'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('delete/', views.delete_from_cart, name='delete_from_cart'),
    path('update/', views.update_cart, name='update_cart'),

]
