from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def login(request):
    return Response({})


# · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 


@api_view(['POST'])
def sing_up(request):
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    user = serializer.save()
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user":UserSerializer(user).data})


# Quick notes

# "Token.objects.get_or_create"
# This method created a new token or gets an existing one. 
# The "create" variable is just a boolean saying if it was created or not
# True if it was indeed created or False if it wasn't

# We're also using "UserSerializer(user).data" because in our serializer
# we set that the password is a write_only field. With this we can control what kind
# of information gets returned in the response


# · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 


@api_view(['GET'])
def test_token(request):
    return Response({})