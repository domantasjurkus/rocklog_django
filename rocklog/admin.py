from django.contrib import admin
from .models import Song, Stream

# Register your models here.
admin.site.register(Song)
admin.site.register(Stream)