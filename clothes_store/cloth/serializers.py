from rest_framework import serializers
from .models import cloth, Client
from django.contrib.auth.models import User

class clothSerializer(serializers.ModelSerializer):
    class Meta:
        model = cloth
        fields = 'all'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        Client
        fields = "all"

class UserSerializer(serializers.ModelSerializer):
    class Mate:
        model = User
        fields = ['id','last_login','is_superuser','username','email','data_joined']
