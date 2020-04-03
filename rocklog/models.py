import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Song(models.Model):
    artist = models.CharField(max_length=128)
    song = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.artist} - {self.song}"

    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    # def save(self):
    #     self.create_at = timezone.now()
    #     return super(Song, self).save()


class StreamEntry(models.Model):
    date = models.DateTimeField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Stream Entries"

    def __str__(self):
        return f"{self.date} - {self.song.artist} - {self.song.song}"


class SavedSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.song.song}"