from django.shortcuts import render

from products.models import Film

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