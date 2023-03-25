from rest_framework import serializers
from .models import ClassGroup


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = "__all__"
