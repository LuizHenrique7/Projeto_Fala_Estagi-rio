from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Estagiario(models.Model):
    nome = models.CharField(max_length=20)
    postagem = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now())



