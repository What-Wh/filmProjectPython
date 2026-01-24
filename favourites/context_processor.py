from favourites.favorites import get_count_of_favorite_films

def favorite_films_count(request):
    count = get_count_of_favorite_films(request)
    return {'favorite_films_count': count}