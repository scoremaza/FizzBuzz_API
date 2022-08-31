from django.urls import path, include
from .views import (
    FizzBuzzViewSet,
)
from rest_framework.routers import DefaultRouter

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'fizzbuzz', FizzBuzzViewSet)

urlpatterns = router.urls