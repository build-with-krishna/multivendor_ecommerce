from django.urls import path
from . import views

urlpatterns = [

    path(
        'create-store/',
        views.create_store,
        name='create_store'
    ),

    path(
        'dashboard/',
        views.vendor_dashboard,
        name='vendor_dashboard'
    ),

]