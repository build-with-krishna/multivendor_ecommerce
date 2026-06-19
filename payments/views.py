from django.shortcuts import render
from .models import Payment


def payment_success(request):

    return render(
        request,
        'payments/payment_success.html'
    )


def payment_failed(request):

    return render(
        request,
        'payments/payment_failed.html'
    )