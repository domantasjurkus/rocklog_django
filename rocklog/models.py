import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Song(models.Model):
    artist = models.CharField(max_length=128)
    song = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.artist} - {self.song}"

    
    def get(artist, song):
        return Song.objects.filter(artist=artist).filter(song=song)

    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    # def save(self):
    #     self.create_at = timezone.now()
    #     return super(Song, self).save()


class StreamEntry(models.Model):
    date = models.DateTimeField(default=timezone.now())
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Stream Entries"

    def __str__(self):
        return f"{self.date} - {self.song.artist} - {self.song.song}"

    
    def is_latest_entry_already_added(song):
        last_entry = StreamEntry.objects.last()
        
        return last_entry.song == song


class SavedSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.song.song}"