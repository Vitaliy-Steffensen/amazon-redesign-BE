from django.urls import path, include
from .views import UserLoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('login', UserLoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]