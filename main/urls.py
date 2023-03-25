from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.LectureListApiView.as_view()),
    path("<int:pk>/", views.LectureDetailApiView.as_view()),
]