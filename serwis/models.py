from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.user.username


class RodzajUsterki(models.Model):
    rodzaj_usterki = models.CharField(max_length=60, unique=False)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.rodzaj_usterki


class Urzadzenie(models.Model):
    nazwa_urzadzenia = models.CharField(max_length=80, unique=False)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa_urzadzenia


class ListaZglaszajacych(models.Model):
    nr_zglaszajacego = models.DecimalField(max_digits=4, decimal_places=0, unique=True)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.nr_zglaszajacego


class ZgloszenieUsterki(models.Model):
    data_zgloszenia = models.DateField('data zgłoszenia')
    czas_zgloszenia = models.TimeField('czas zgłoszenia')
    zglaszajacy = models.DecimalField(max_digits=4, decimal_places=0, unique=True)
    temat_zgloszenia = models.CharField(max_length=400, unique=False)
    rodzaj_usterki = models.ForeignKey(RodzajUsterki, on_delete=models.CASCADE, default=1)
    urzadzenie = models.ForeignKey(Urzadzenie, on_delete=models.CASCADE, default=1)
    opis_zgloszenia = models.TextField()
    status = models.DecimalField(max_digits=1, decimal_places=0)
    data_otwarcia = models.DateField('data otwarcia')
    czas_otwarcia = models.TimeField('czas otwarcia')
    serwisant = models.ForeignKey(Autor, on_delete=models.CASCADE, default=1)
    opis_rozwiazania = models.TextField()
    data_zamkniecia = models.DateField('data zamknięcia')
    czas_zamkniecia = models.TimeField('czas zamknięcia')

    def __str__(self):
        return self.temat_zgloszenia