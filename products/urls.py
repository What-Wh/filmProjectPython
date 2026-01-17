from django.urls import path, include
from products import views

urlpatterns = [
    path('film/<int:id>/', views.oneProductPage),
    path('delete/<int:id>/', views.deleteProduct),
    path('list/', views.list_of_films, name="film_list"),
    path('create/', views.create_film, name='create_film'),
    path('update/<int:id>/', views.update_film, name="update_film")
]