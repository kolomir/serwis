from django.shortcuts import render, redirect
from .models import ZgloszenieUsterki, ListaZglaszajacych, Urzadzenie, RodzajUsterki, Autor
from .forms import ZgloszenieForm, RodzajUsterkiForm, UrzadzenieForm, ListaZglaszajacychForm
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
#  Formularze Rodzajów Usterek
#---------------------------------------------------
@login_required
def nowy_RodzajUsterek(request):
    form_RodzajUsterki = RodzajUsterkiForm(request.POST or None, request.FILES or None)
    rodzaj_usterki = RodzajUsterki.objects.all().order_by('rodzaj_usterki')

    if form_RodzajUsterki.is_valid():
        form_RodzajUsterki.save()
        return redirect(nowy_RodzajUsterek)

    context = {
        'form_RodzajUsterki': form_RodzajUsterki,
        'rodzaj_usterki': rodzaj_usterki
    }
    return render(request, 'serwis/nowy_rodzaj_usterki.html', context)


#---------------------------------------------------
#  Formularz do wprowadzania Maszyn i Urządzeń do bazy
#---------------------------------------------------
@login_required
def nowe_Urzadzenie(request):
    form_Urzadzenia = UrzadzenieForm(request.POST or None, request.FILES or None)

    if form_Urzadzenia.is_valid():
        form_Urzadzenia.save()
        return redirect(nowe_zgloszenia)

    context = {
        'form_Urzadzenia': form_Urzadzenia
    }
    return render(request, 'serwis/form_urzadzenie.html', context)


#---------------------------------------------------
#  Formularz do wprowadzania Maszyn i Urządzeń do bazy
#---------------------------------------------------
@login_required
def nowy_Zglaszajacy(request):
    form_Zglaszajacy = ListaZglaszajacychForm(request.POST or None, request.FILES or None)

    if form_Zglaszajacy.is_valid():
        form_Zglaszajacy.save()
        return redirect(nowy_Zglaszajacy)

    context = {
        'form_Zglaszajacy': form_Zglaszajacy
    }
    return render(request, 'serwis/form_zglaszajacy.html', context)


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

def test(request):
    return render(request, 'serwis/test.html')