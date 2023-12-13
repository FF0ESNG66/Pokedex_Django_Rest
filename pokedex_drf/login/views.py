from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404



# · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    return Response({"Success": f"Welcome back {user.username}", "token": token.key})

# Quick notes

# Here again we're using get_or_create just in case if for some reason the token wasn't created in the register view

# Notice that in line 12 we're using 404 response but also in line 14. This is because we want to use the SAME response if the username is wrong or
# if the password is wrong for security reasons. We wouldn't want to give any sort of information

# If everything is okay we will get a token to use in other requests among the APIs


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
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Passed for {}".format(request.user.username))


# Quick notes

# Those decorators follow the same logic as when we apply authentication_classes and permission_classes
# in generics class_based views