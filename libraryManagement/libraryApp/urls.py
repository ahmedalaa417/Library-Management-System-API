from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]