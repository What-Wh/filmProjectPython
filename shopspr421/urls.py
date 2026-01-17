from django.contrib import admin
from django.urls import path, include

from shopspr421 import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('films/', include('products.urls')),
    path('favorites/', include('favourites.urls')),
]

if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)