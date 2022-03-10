from .models import Product, ProductCategory, HotProduct
from .serializers import HotProductSerializer, PreviewProductSerializer, SearchProductSerializer, DetailedProductSerializer, ProductCategorySerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

class PreviewProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = PreviewProductSerializer   

class SearchProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer    


class DetailedProductViewSet(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = DetailedProductSerializer

    lookup_field = 'id'   

    def get(self, request, id):
        return self.retrieve(request, id=id)

class ProductCategoriesViewSet(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class HotProductViewSet(generics.ListAPIView):
    queryset = HotProduct.objects.all()
    serializer_class = HotProductSerializer
