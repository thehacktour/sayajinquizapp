from .models import QuizModel
from .serializers import QuizSerializer
from rest_framework import viewsets
from rest_framework import permissions

class QuizEndPoint(viewsets.ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer