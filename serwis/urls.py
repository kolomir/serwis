from django.urls import path, include
from .views import nowe_zgloszenia, test, nowy_RodzajUsterek


urlpatterns = [
    path('', nowe_zgloszenia, name='nowe_zgloszenia'),
    path('nowy_rodzaj_usterki/', nowy_RodzajUsterek, name='nowy_rodzaj_usterki'),

    path('test/', test, name='test'),
    ]