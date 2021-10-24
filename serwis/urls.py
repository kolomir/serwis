from django.urls import path, include
from .views import nowe_zgloszenia, test, nowy_RodzajUsterek, nowe_Urzadzenie


urlpatterns = [
    path('', nowe_zgloszenia, name='nowe_zgloszenia'),
    path('nowy_rodzaj_usterki/', nowy_RodzajUsterek, name='nowy rodzaj usterki'),
    path('nowe_urzadzenia/', nowe_Urzadzenie, name='nowe urzadzenia'),

    path('test/', test, name='test'),
    ]