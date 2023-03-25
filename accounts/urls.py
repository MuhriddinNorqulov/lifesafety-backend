from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view()),
    path("register/", views.UserRegistrationAPIVIew.as_view()),
    path("groups-all/", views.GroupsAll.as_view())

]