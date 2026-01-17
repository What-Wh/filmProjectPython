FAVORITE_FILMS_KEY = 'favorite_film'

def get_favorites_films(request):
    return request.session.get(FAVORITE_FILMS_KEY, [])

def get_count_of_favorite_films(request):
    return len(get_favorites_films(request))

def add_film_to_favorites(request, film_id):
    favoritesIds = get_favorites_films(request)
    if film_id not in favoritesIds:
        favoritesIds.append(film_id)
        request.session[FAVORITE_FILMS_KEY] = favoritesIds
    request.session.modified = True

def remove_film_from_favorites(request, film_id):
    favoritesIds = get_favorites_films(request)
    if film_id in favoritesIds:
        favoritesIds.remove(film_id)
        request.session[FAVORITE_FILMS_KEY] = favoritesIds
    request.session.modified = True