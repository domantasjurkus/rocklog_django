import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    date = models.DateTimeField('date published')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="hamster")
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice