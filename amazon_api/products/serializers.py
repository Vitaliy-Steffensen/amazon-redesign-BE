from pickletools import read_floatnl
from rest_framework import serializers
from .models import Product, ProductImage, ProductFeature, ProductCategory, HotProduct

class SearchProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'thumbnail']

class PreviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'rating', 'thumbnail', 'category']
        

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'

class DetailedProductSerializer(serializers.ModelSerializer):
    images=ProductImageSerializer(read_only=True,many=True)
    features=ProductFeaturesSerializer(read_only=True,many=True)
    related_products=PreviewProductSerializer(read_only=True,many=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'rating', 'thumbnail', 'description', 'stock', 'sku', 'images', 'features', 'related_products']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class HotProductSerializer(serializers.ModelSerializer):
    product=PreviewProductSerializer()
    class Meta:
        model = HotProduct
        fields = ['id', 'product']