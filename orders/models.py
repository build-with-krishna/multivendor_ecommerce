from django.db import models
from accounts.models import User
from products.models import Product

STATUS_CHOICES = (

    ('Pending','Pending'),
    ('Confirmed','Confirmed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')

)


class Order(models.Model):

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    city = models.CharField(max_length=100)

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.id)



class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return self.product.name