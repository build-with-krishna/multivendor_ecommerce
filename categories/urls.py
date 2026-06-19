from django.urls import path
from . import views

urlpatterns = [

    path(
        'categories/',
        views.category_list,
        name='category_list'
    ),

    path(
        'add-category/',
        views.add_category,
        name='add_category'
    ),

]