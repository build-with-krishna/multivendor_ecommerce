from django.db import models
from accounts.models import User

class Vendor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    store_name = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to='vendors/',
        blank=True,
        null=True
    )

    gst_number = models.CharField(max_length=50)

    pan_number = models.CharField(max_length=50)

    address = models.TextField()

    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name