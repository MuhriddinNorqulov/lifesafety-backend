from rest_framework import serializers
from .models import *


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['title', 'image', 'url']


class ControlQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlQuestion
        fields = ['question']


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ["id", "title"]


class LectureDetailSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField(read_only=True)
    questions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lecture
        fields = ["id", "title", "text", "youtube", "resources", "questions"]


    def get_resources(self, obj):
        data = Resource.objects.filter(lecture=obj).order_by('id')
        return ResourceSerializer(data, many=True)

    def get_questions(self, obj):
        data = ControlQuestion.objects.filter(lecture=obj).order_by('id')
        return ControlQuestionSerializer(data, many=True).data
