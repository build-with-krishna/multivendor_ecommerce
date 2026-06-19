from django.urls import path
from . import views

urlpatterns = [

    path(
        'vendor-dashboard/',
        views.vendor_dashboard,
        name='vendor_dashboard'
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

]