from .models import Product, ProductCategory, HotProduct
from .serializers import HotProductSerializer, PreviewProductSerializer, SearchProductSerializer, DetailedProductSerializer, ProductCategorySerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
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


stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
def StripeIntentView(request):
    try:
        total = int(request.data["total"])
        currency = request.data["currency"]
        custommer_email = request.data["email"]

        if not total or not currency or not custommer_email:
            return Response({"error":"Please fill all fields"}, status=status.HTTP_400_BAD_REQUEST)

        customer = stripe.Customer.create(email=custommer_email)

        intent = stripe.PaymentIntent.create(
            amount=total,
            currency=currency,
            payment_method_types=["card"],
            customer=customer
        )

        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({ 'error': str(e) })
    
