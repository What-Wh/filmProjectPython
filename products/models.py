from django.db import models

# Create your models here.
class Film(models.Model):
    GENRE_CHOICES = [
    ('action', 'Action'),
    ('fantasy', 'Fantasy'),
    ('comedy', 'Comedy'),
    ('drama', 'Drama'),
    ('horror', 'Horror'),
    ('sci-fi', 'Sci-Fi'),
    ('romance', 'Romance'),
    ('thriller', 'Thriller'),
    ('documentary', 'Documentary'),
    ('animation', 'Animation'),
    ('adventure', 'Adventure'),
    ('mystery', 'Mystery'),
    ('crime', 'Crime'),
    ('musical', 'Musical'),
    ('biography', 'Biography'),
    ('war', 'War'),
    ('western', 'Western'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='films_images/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    mark = models.IntegerField()
    year = models.IntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    def __str__(self):
        return self.title