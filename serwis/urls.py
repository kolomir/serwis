from django.urls import path, include
from .views import nowe_zgloszenia


urlpatterns = [
    path('', nowe_zgloszenia, name='nowe_zgloszenia'),
    ]