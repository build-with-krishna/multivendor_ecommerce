from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'add-product/',
        views.add_product,
        name='add_product'
    ),

]