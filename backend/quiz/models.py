from django.db import models

class QuizModel(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    nome = models.TextField(max_length=255)

    