from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogpost
from .serializers import BlogpostSerializers

class BlogpostView(generics.ListCreateAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=BlogpostSerializers

    def delete(self, request, *args, **kwrgs):
          Blogpost.objects.all().delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

class Blogpostupdatedestry(generics.RetrieveUpdateDestroyAPIView):
        queryset=Blogpost.objects.all()
        serializer_class=BlogpostSerializers
        lookup_field="pk"
