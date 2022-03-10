from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


class Ratings(models.IntegerChoices):
    VERY_LOW = 1, 'Very low'
    LOW = 2, 'Low'
    NORMAL = 3, 'Normal'
    HIGH = 4, 'High'
    VERY_HIGH = 5, 'Very high'



def upload_to(instance, filename):
    return 'products-images/{filename}'.format(filename=filename)

class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='products-images/default.jpg')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    rating = models.IntegerField(default=Ratings.HIGH, choices=Ratings.choices)
    thumbnail = models.ImageField(_("Image"), upload_to=upload_to, default='products-images/default.jpg')
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE, default=None,  related_name='category'
    )
    description = models.TextField()
    stock = models.IntegerField(default=0)
    sku = models.BigIntegerField(default=0)
    related_products = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return "{} {}".format(self.pk, self.title)

class ProductImage(models.Model):
    product = models.ForeignKey(         
        Product,
        on_delete=models.CASCADE, default=None,  related_name='images')
    image = models.ImageField(_("Image"), upload_to=upload_to, default='products-images/default.jpg')

class ProductFeature(models.Model):
    product = models.ForeignKey(         
        Product,
        on_delete=models.CASCADE, default=None,  related_name='features')
    title = models.CharField(max_length=100)

class HotProduct(models.Model):
    product = models.ForeignKey(         
        Product,
        on_delete=models.CASCADE, default=None,  related_name='hot_product')
