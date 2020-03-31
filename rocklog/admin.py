from django.contrib import admin
from .models import Song, StreamSong, SavedSong

# Register your models here.
admin.site.register(Song)
admin.site.register(StreamSong)
admin.site.register(SavedSong)
