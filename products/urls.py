


from django.urls import path, include

from products import views


urlpatterns = [
    path('', views.index),
    path('film/<int:id>/', views.oneProductPage),
    path('delete/<int:id>/', views.deleteProduct),
]