
from django.urls import path
from favourites import views


urlpatterns =[
    path('add/<int:film_id>/<str:return_url>/', views.add_film,
        name='add_fav_film'),
    path('remove/<int:film_id>/<str:return_url>/', views.remove_film,
        name='remove_fav_film'), 
]