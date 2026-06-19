from django.db import models
from vendors.models import Vendor
from categories.models import Category,SubCategory,Brand


class Product(models.Model):

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='products/'
    )

    description = models.TextField()

    sku = models.CharField(
        max_length=100,
        unique=True
    )

    barcode = models.CharField(
        max_length=100,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    stock = models.IntegerField(default=0)

    featured = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name