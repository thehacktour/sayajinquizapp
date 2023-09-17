from .models import QuizModel
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = "__all__"