from django.db import models
from accounts.models import User
from songs.models import Song
# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "playlist"
        verbose_name_plural = "play list table"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "the user who liked it"
        verbose_name_plural = "liked history"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.TextField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} commented on {self.song} song"

    class Meta:
        verbose_name = "the comment"
        verbose_name_plural = "comment history"

