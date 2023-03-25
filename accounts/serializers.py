from rest_framework import serializers
from django.conf import settings
from .models import CustomUser
from groups.serializers import GroupSerializer, ClassGroup


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "phone_number", "password", "group"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = CustomUser(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


