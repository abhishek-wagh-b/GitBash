from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogpost
from .serializers import BlogpostSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializers, LoginSerializers, Userserializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser] 

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

class BlogpostView(generics.ListCreateAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=BlogpostSerializers
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwrgs):
        if not request.user.is_staff:
            return Response({"detail": "Only admins can delete."}, status=status.HTTP_403_FORBIDDEN)
        

class Blogpostupdatedestry(generics.RetrieveUpdateDestroyAPIView):
        queryset=Blogpost.objects.all()
        serializer_class=BlogpostSerializers
        lookup_field="pk"
        permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes= (AllowAny,)
    serializer_class= RegisterSerializers

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        username= request.data.get("username")
        password= request.data.get("password")
        user=authenticate(username=username, password=password)

        if user is not None:
            refresh=RefreshToken.for_user(user)
            User_serializer= Userserializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': User_serializer.data
            })
        else :
            return Response({'details: details not found'}, status=401)        