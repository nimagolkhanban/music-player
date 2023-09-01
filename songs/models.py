from django.db import models
from artists.models import Artist
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories table"


class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    upload_date = models.DateField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to='songs/')
    audio_file = models.FileField(upload_to='songs/')
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "song"
        verbose_name_plural = "songs"
