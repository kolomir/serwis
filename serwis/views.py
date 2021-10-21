from django.shortcuts import render, redirect
from .models import ZgloszenieUsterki, ListaZglaszajacych, Urzadzenie, RodzajUsterki, Autor
from .forms import ZgloszenieForm, RodzajUsterkiForm
from datetime import datetime
from django.contrib.auth.decorators import login_required


#---------------------------------------------------
# pobieranie informacji o osobie zalogowaniej
#---------------------------------------------------
def get_author(user):
    qs = Autor.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


#---------------------------------------------------
#  Formularz do wprowadzania Rodzajów Usterek
#---------------------------------------------------
@login_required
def nowy_RodzajUsterek(request):
    form_RodzajUsterki = RodzajUsterkiForm(request.POST or None, request.FILES or None)

    if form_RodzajUsterki.is_valid():
        form_RodzajUsterki.save()
        return redirect(nowe_zgloszenia)

    context = {
        'form_RodzajUsterki': form_RodzajUsterki
    }
    return render(request, 'serwis/form_rodzaj_usterek.html', context)



#---------------------------------------------------
# widok pierwszej strony
# wszystkie dodane i nie podjęte jeszcze zgłoszenia
#---------------------------------------------------
def nowe_zgloszenia(request):
    noweZgloszenia = ZgloszenieUsterki.objects.filter(status=0).order_by('-id')

    context = {
        'nowe_zgloszenia': noweZgloszenia
    }

    return render(request, 'serwis/nowe_zgloszenia.html', context)


def dodaj_zgloszenie(request):
    form_zgloszenie = ZgloszenieForm(request.POST or None, request.FILES or None)
    data_teraz = datetime.now()
    data_zgloszenia = data_teraz.strftime("%Y-%m-%d")

    if form_zgloszenie.is_valid():
        form_zgloszenie.save()
        return redirect(nowe_zgloszenia)

    context = {
        'form_zgloszenie': form_zgloszenie
    }

    return render(request, 'serwis/nowe_zgloszenia.html', context)

