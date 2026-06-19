from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='category/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name



class SubCategory(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name



class Brand(models.Model):

    name = models.CharField(max_length=100)

    logo = models.ImageField(
        upload_to='brand/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name