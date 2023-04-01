from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.


class LectureListApiView(generics.ListAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        lecture_type = query_params.get("type")
        print(lecture_type)
        if lecture_type == "practice":
            return Lecture.objects.filter(type="practice")
        return Lecture.objects.filter(type="lecture")


# class LectureDetailApiView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         lecture_id = kwargs.get("pk")
#         lecture = Lecture.objects.get(id=lecture_id)
#
#         if lecture is None:
#             return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = LectureDetailSerializer(lecture, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class LectureDetailApiView(generics.RetrieveAPIView):
    serializer_class = LectureDetailSerializer
    queryset = Lecture.objects.all()



