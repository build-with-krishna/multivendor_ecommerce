from django.urls import path
from . import views

urlpatterns = [

    path(
        'add-cart/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    path(
        'remove-cart/<int:id>/',
        views.remove_cart,
        name='remove_cart'
    ),

]