from django.shortcuts import get_object_or_404, render, redirect
from products.forms.film import FilmForm

from products.models import Film

import home

# Create your views here.
def list_of_films(request):
    films = Film.objects.all()
    return render(request, 'products/list.html', {'films': films})

def oneProductPage(request, id):
    film = Film.objects.get(pk=id)
    return render(request, 'products/oneProductPage.html', {'film' : film})

def deleteProduct(request, id):
    film = Film.objects.get(pk=id)
    film.delete()
    films = Film.objects.all()
    return render(request, 'products/list.html', {'films': films})

def create_film(request):
    if request.method == 'POST':
        film_form = FilmForm(request.POST)
        if film_form.is_valid():
            film_form.save()
            return redirect('film_list')
    film_form = FilmForm()
    return render(request, 'products/createPage.html', {'form': film_form})

def update_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == 'POST':
        film_form = FilmForm(request.POST, instance=film)
        if film_form.is_valid():
            film_form.save()
            return redirect('film_list')
    film_form = FilmForm(instance=film)
    return render(request, 'products/updatePage.html', {'form': film_form})