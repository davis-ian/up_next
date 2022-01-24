from rest_framework import serializers
from accounts.models import CustomUser
from watch.models import Movie

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'id',
        )
        model = CustomUser

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'release',
            'category',
            'id',
        )
        model = Movie