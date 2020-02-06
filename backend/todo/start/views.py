from django.shortcuts import render
from rest_framework import generics

from .models import todoList
from .serializer import todoListSerializer


class ListtodoList(generics.ListCreateAPIView):
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer


class DetailtodoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer
