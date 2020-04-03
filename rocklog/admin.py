from django.contrib import admin
from .models import Song, StreamEntry, SavedSong

# Register your models here.
admin.site.register(Song)
admin.site.register(StreamEntry)
admin.site.register(SavedSong)
