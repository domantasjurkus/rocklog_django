from django.contrib import admin
from .models import Song, StreamSong

# Register your models here.
admin.site.register(Song)
admin.site.register(StreamSong)
