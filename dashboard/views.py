from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from vendors.models import Vendor
from products.models import Product
from orders.models import OrderItem


from accounts.models import User
from vendors.models import Vendor
from products.models import Product
from orders.models import Order


@login_required
def vendor_dashboard(request):

    try:
        vendor = Vendor.objects.get(user=request.user)
    except Vendor.DoesNotExist:
        return redirect('create_store')

    if not vendor.approved:
        return render(request,'vendors/pending.html')

    total_products = Product.objects.filter(
        vendor=vendor
    ).count()

    order_items = OrderItem.objects.filter(
        product__vendor=vendor
    )

    total_orders = order_items.count()

    revenue = 0

    for item in order_items:

        revenue += item.price * item.quantity

    low_stock = Product.objects.filter(
        vendor=vendor,
        stock__lt=10
    )

    context = {

        'total_products': total_products,

        'total_orders': total_orders,

        'revenue': revenue,

        'low_stock': low_stock

    }

    return render(
        request,
        'dashboard/vendor_dashboard.html',
        context
    )



@login_required
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('home')

    total_vendors = Vendor.objects.count()

    total_customers = User.objects.filter(
        role='customer'
    ).count()

    total_products = Product.objects.count()

    total_orders = Order.objects.count()

    total_revenue = sum(
        order.total_amount for order in Order.objects.all()
    )

    pending_vendors = Vendor.objects.filter(
        approved=False
    )

    recent_orders = Order.objects.order_by(
        '-id'
    )[:10]

    context = {

        'total_vendors': total_vendors,
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_vendors': pending_vendors,
        'recent_orders': recent_orders

    }

    return render(
        request,
        'dashboard/admin_dashboard.html',
        context
    )