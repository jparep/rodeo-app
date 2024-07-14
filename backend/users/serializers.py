from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_contestant', 'is_admin', 'is_staff', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined']
