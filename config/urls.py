from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/',admin.site.urls),

    path('',include('accounts.urls')),

    path('',include('vendors.urls')),

    path('',include('categories.urls')),

    path('',include('products.urls')),

    path('',include('cart.urls')),

    path('',include('orders.urls')),

    path('',include('payments.urls')),

    path('',include('dashboard.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )