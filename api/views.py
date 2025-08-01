from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogpost
from .serializers import BlogpostSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import IsAdminUser

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