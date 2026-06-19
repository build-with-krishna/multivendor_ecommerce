from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        cart[product_id]['quantity'] += 1

    else:
        cart[product_id] = {

            'name': product.name,
            'price': float(
                product.discount_price
                if product.discount_price > 0
                else product.price
            ),

            'quantity': 1,

            'image': product.image.url

        }

    request.session['cart'] = cart

    return redirect('cart')


def cart_view(request):

    cart = request.session.get('cart', {})

    total = 0

    for item in cart.values():
        total += item['price'] * item['quantity']

    context = {

        'cart': cart,
        'total': total

    }

    return render(
        request,
        'cart/cart.html',
        context
    )


def remove_cart(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart

    return redirect('cart')