from rest_framework import serializers
from .models import Blogpost
from django.contrib.auth.models import User

class BlogpostSerializers(serializers.ModelSerializer):
    class Meta:
        model= Blogpost
        fields= ["id", "title", "content", "published_date"]


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["id","username","email","date_joined"]  

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["username","email","password"]        

    def create(self, Validated_user):
        user= User.objects.create_user(
            Validated_user["username"],
            Validated_user["email"],
            Validated_user["password"],
        )    
        return user
    
class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password= serializers.CharField(required=True, write_only=True)   
