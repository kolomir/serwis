from django.forms import ModelForm
from django import forms
from .models import ZgloszenieUsterki, ListaZglaszajacych, Urzadzenie, RodzajUsterki, Autor


class ZgloszenieForm(ModelForm):
    class Meta:
        model = ZgloszenieUsterki
        fields = [
            'data_zgloszenia',
            'czas_zgloszenia',
            'zglaszajacy',
            'temat_zgloszenia',
            'rodzaj_usterki',
            'urzadzenie',
            'opis_zgloszenia',
            'status',
            'data_otwarcia',
            'czas_otwarcia',
            'serwisant',
            'opis_rozwiazania',
            'data_zamkniecia',
            'czas_zamkniecia'
        ]