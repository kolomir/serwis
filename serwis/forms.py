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


class ListaZglaszajacychForm(ModelForm):
    class Meta:
        model = ListaZglaszajacych
        fields = [
            'nr_zglaszajacego',
            'aktywny'
        ]


class UrzadzenieForm(ModelForm):
    class Meta:
        model = Urzadzenie
        fields = [
            'nazwa_urzadzenia',
            'aktywny'
        ]


class RodzajUsterkiForm(ModelForm):
    class Meta:
        model = RodzajUsterki
        fields = [
            'rodzaj_usterki',
            'aktywny'
        ]