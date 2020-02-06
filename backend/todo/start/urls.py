from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListtodoList.as_view()),
    path('<int:pk>/', views.DetailtodoList.as_view()),
    ]