from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'is_contestant', 'is_admin', 
            'is_staff', 'is_active', 'date_joined'
        ]
        read_only_fields = [
            'id', 'is_staff', 'is_active', 'date_joined'
        ]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'password', 'is_contestant', 'is_admin'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            is_contestant=validated_data['is_contestant'],
            is_admin=validated_data['is_admin']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
