from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.user.username


class RodzajUsterki(models.Model):
    rodzaj_usterki = models.CharField(max_length=60, unique=False)
    aktywny = models.BooleanField(default=True)
