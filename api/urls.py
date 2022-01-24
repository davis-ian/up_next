from django.urls import path

from .views import MovieViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = router.urls