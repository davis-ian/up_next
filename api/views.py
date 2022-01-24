from django.shortcuts import render
from accounts.models import CustomUser
from rest_framework import generics, viewsets
from watch.models import Movie
from .serializers import CustomUserSerializer, MovieSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer