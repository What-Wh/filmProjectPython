from django.shortcuts import render

from favourites.favorites import get_count_of_favorite_films, get_favorites_films

from products.models import Film

# Create your views here.
def index(request, filter_by_favorites=False):
    films = Film.objects.all()
    if filter_by_favorites:
        fav_ids = get_favorites_films(request)
        films = films.filter(id__in=fav_ids)
    
    return render(request, 'home/index.html', {
        'films': films, 
        "fav_count": get_count_of_favorite_films(request),
        "fav_ids": get_favorites_films(request),
    })
