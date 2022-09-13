from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, FavouritesSerializer
from django.http import HttpResponse
from .models import CustomUser, Favourites


# set up user login and user registration
@api_view(['GET', 'POST'])
def apply_for_funding(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_user_favourites(request):
    if request.method == 'GET':
        favourites = Favourites.objects.all()
        serializer = FavouritesSerializer(favourites, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FavouritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
