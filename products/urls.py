


from django.urls import path, include

from products import views


urlpatterns = [
    path('film/<int:id>/', views.oneProductPage),
    path('delete/<int:id>/', views.deleteProduct),
    path('list/', views.list_of_films, name="film_list"),
]