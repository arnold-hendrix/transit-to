from rest_framework import serializers
from .models import CustomUser, Favourites


class UserSerializer(serializers.ModelSerializer):
    favourites = serializers.PrimaryKeyRelatedField(many=True, queryset=Favourites.objects.all())

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'favourites')


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('user', 'locations')
