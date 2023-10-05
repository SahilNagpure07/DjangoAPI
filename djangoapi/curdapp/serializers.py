from django.db.models import fields
from rest_framework import serializers
from .models import users

class usersserializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('id', 'name', 'email', 'password')