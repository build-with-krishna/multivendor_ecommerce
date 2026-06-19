from django.db import models
from orders.models import Order

PAYMENT_METHODS = (

    ('COD','Cash On Delivery'),
    ('RAZORPAY','Razorpay')

)

PAYMENT_STATUS = (

    ('Pending','Pending'),
    ('Success','Success'),
    ('Failed','Failed')

)


class Payment(models.Model):

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    transaction_id = models.CharField(
        max_length=200,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.order.id)