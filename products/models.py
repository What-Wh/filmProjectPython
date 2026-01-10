from django.db import models

# Create your models here.
class Film(models.Model):
    GENRE_CHOICES = [
    ('action', 'Action'),
    ('fantasy', 'Fantasy')]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='films_images/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mark = models.IntegerField()
    year = models.IntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    def __str__(self):
        return self.title