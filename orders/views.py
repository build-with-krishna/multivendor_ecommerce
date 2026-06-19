from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Order,OrderItem
from products.models import Product
from payments.models import Payment

@login_required
def checkout(request):

    cart = request.session.get('cart', {})

    total = 0

    for item in cart.values():

        total += item['price'] * item['quantity']

    if request.method == "POST":

        order = Order.objects.create(

            customer=request.user,

            name=request.POST['name'],

            phone=request.POST['phone'],

            address=request.POST['address'],

            city=request.POST['city'],

            total_amount=total

        )

        for key,item in cart.items():

            product = Product.objects.get(id=key)

            OrderItem.objects.create(

                order=order,

                product=product,

                quantity=item['quantity'],

                price=item['price']

            )

            product.stock -= item['quantity']

            product.save()

            Payment.objects.create(

                order=order,

                payment_method='COD',

                amount=total,

                payment_status='Success'

            )

        request.session['cart'] = {}

        return redirect('payment_success')

    return render(
        request,
        'orders/checkout.html',
        {
            'total':total
        }
    )


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by('-id')

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders':orders
        }
    )