from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from groups.models import ClassGroup
from groups.serializers import GroupSerializer


class GroupsAll(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = ClassGroup.objects.all()



class UserRegistrationAPIVIew(generics.CreateAPIView):
    serializer_class = UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #
    #     # Add custom claims
    #     token['name'] = user.username
    #     token['key'] = 'val'
    #     # ...
    #
    #     return token

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializer(self.user).data
        self.user.last_login = datetime.now()
        self.user.save()
        # del data['refresh']
        for key, val in serializer.items():
            data[key] = val

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
