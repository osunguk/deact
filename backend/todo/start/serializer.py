from rest_framework import serializers
from .models import todoList


class todoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name'
        )
        model = todoList

