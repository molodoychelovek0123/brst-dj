from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Collection(models.Model):
    title = models.CharField(max_length=200)
    main_picture = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Collections"


class Type(models.Model):
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_info = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Types'


class Product(models.Model):
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sleeve = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    quantity = models.IntegerField()
    size = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.type.title) + " " + str(self.sleeve) + " " + str(self.material) + " " + str(self.size)

    class Meta:
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id])


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=True)
    image = models.FileField(upload_to='shop/img/products/', default=None)


class Lookbook(models.Model):
    title = models.CharField(max_length=200)
    main_picture = models.CharField(max_length=200)
    pictures = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Lookbooks"

