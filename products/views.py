from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from vendors.models import Vendor
from .models import Product
from .forms import ProductForm


@login_required
def add_product(request):

    vendor = Vendor.objects.get(user=request.user)

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.vendor = vendor

            product.save()

            return redirect('product_list')

    else:

        form = ProductForm()

    return render(
        request,
        'products/add_product.html',
        {
            'form':form
        }
    )


def product_list(request):

    products = Product.objects.filter(active=True)

    return render(
        request,
        'products/product_list.html',
        {
            'products':products
        }
    )


from categories.models import Category

def home(request):

    featured_products = Product.objects.filter(
        featured=True,
        active=True
    )[:8]

    latest_products = Product.objects.filter(
        active=True
    ).order_by('-id')[:8]

    categories = Category.objects.all()

    context = {

        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories

    }

    return render(
        request,
        'home.html',
        context
    )


def product_detail(request,id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        'products/product_detail.html',
        {
            'product':product
        }
    )