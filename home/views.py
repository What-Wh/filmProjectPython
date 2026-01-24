from django.shortcuts import render

from favourites.favorites import get_favorites_films

from products.models import Film

# Create your views here.
def index(request, filter_by_favorites=False):
    films = Film.objects.all()

    filter_text = request.GET.get("filter_text", "")

    if filter_by_favorites:
        fav_ids = get_favorites_films(request)
        films = films.filter(id__in=fav_ids)

    if filter_text:
        films = films.filter(title__icontains=filter_text)
    
    return render(request, 'home/index.html', {
        'films': films, 
        "fav_ids": get_favorites_films(request),
    })
