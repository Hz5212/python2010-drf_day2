from django.urls import path

from api import views

urlpatterns = [
    path("users/", views.UserAPIView.as_view()),
    path("users/<str:id>/", views.UserAPIView.as_view()),
    path("student/", views.StudentAPIView.as_view()),
    path("student/<str:id>/", views.StudentAPIView.as_view()),
]
