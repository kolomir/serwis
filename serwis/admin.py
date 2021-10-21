from django.contrib import admin
from .models import ZgloszenieUsterki, ListaZglaszajacych, Urzadzenie, RodzajUsterki, Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'serwisant')
    list_filter = ('serwisant', 'aktywny')


@admin.register(RodzajUsterki)
class RodzajUsterki(admin.ModelAdmin):
    list_display = ('rodzaj_usterki', 'aktywny')
    list_filter = ('aktywny',)
    search_fields = ('rodzaj_usterki', 'aktywny')


@admin.register(Urzadzenie)
class Urzadzenie(admin.ModelAdmin):
    list_display = ('nazwa_urzadzenia', 'aktywny')
    list_filter = ('aktywny',)
    search_fields = ('nazwa_urzadzenia', 'aktywny')


@admin.register(ListaZglaszajacych)
class ListaZglaszajacych(admin.ModelAdmin):
    list_display = ('nr_zglaszajacego', 'aktywny')
    list_filter = ('aktywny',)
    search_fields = ('nr_zglaszajacego', 'aktywny')


@admin.register(ZgloszenieUsterki)
class ZgloszenieUsterki(admin.ModelAdmin):
    list_display = ('data_zgloszenia', 'czas_zgloszenia', 'zglaszajacy', 'temat_zgloszenia', 'rodzaj_usterki', 'urzadzenie', 'status', 'data_otwarcia', 'czas_otwarcia', 'serwisant', 'data_zamkniecia', 'czas_zamkniecia')
    list_filter = ('rodzaj_usterki', 'urzadzenie', 'status', 'serwisant')
    search_fields = ('data_zgloszenia', 'czas_zgloszenia', 'zglaszajacy', 'temat_zgloszenia', 'rodzaj_usterki', 'urzadzenie', 'status', 'data_otwarcia', 'czas_otwarcia', 'serwisant', 'data_zamkniecia', 'czas_zamkniecia')

