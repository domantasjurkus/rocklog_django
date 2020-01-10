import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# class Question(models.Model):
#     date = models.DateTimeField('date published')
#     text = models.CharField(max_length=200)

#     def __str__(self):
#         return self.text

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.date <= now


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     # question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="hamster")
#     choice = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice


class Song(models.Model):
    created_at = models.DateTimeField(editable=False)
    artist = models.CharField(max_length=128)
    song = models.CharField(max_length=128)

    def __str__(self):
        return self.song

    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    def save(self):
        self.create_at = timezone.now()
        return super(Song, self).save()


class Stream(models.Model):
    date = models.DateTimeField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song
