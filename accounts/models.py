from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('vendor', 'Vendor'),
    ('customer', 'Customer'),
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    mobile = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email