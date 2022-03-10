from itertools import product
from re import A
from django.contrib import admin
from .models import Product, ProductImage, ProductFeature, ProductCategory, ProductCategory, HotProduct

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_filter = ('title', 'price', 'rating', 'thumbnail', 'category', 'description', 'stock', 'sku', 'related_products')
    list_display = ('title', 'price', 'rating', 'thumbnail', 'category', 'description', 'stock', 'sku')


@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    list_filter = ('product', 'image')
    list_display = ('product', 'image')

@admin.register(ProductFeature)
class ProductFeature(admin.ModelAdmin):
    list_filter = ('product', 'title')
    list_display = ('product', 'title')

@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_filter = ('id', 'title', 'image')
    list_display = ('id', 'title', 'image')
@admin.register(HotProduct)
class HotProduct(admin.ModelAdmin):
    list_filter = ('id', 'product')
    list_display = ('id', 'product')
