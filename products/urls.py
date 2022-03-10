from django.urls import path, include
from .views import PreviewProductViewSet, SearchProductViewSet, DetailedProductViewSet, ProductCategoriesViewSet, HotProductViewSet

urlpatterns = [
    path('search-products/', SearchProductViewSet.as_view(), name='search_products'),
    path('preview-products/', PreviewProductViewSet.as_view(), name='preview_products'),
    path('detailed-products/<int:id>/', DetailedProductViewSet.as_view(), name='detailed_products'),
    path('categories/', ProductCategoriesViewSet.as_view(), name='categories'),
    path('hot-products/', HotProductViewSet.as_view(), name='hot_products'),
]



