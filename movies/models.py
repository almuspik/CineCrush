from django.db import models
from django.contrib.auth.models import User

class SavedMovie(models.Model):
    CATEGORY_CHOICES = [
        ('anime', 'Anime'),
        ('movie', 'Movie'),
        ('series', 'Series'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField()
    poster = models.URLField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
