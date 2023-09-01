from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='artists/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists table"

