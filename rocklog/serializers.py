from rest_framework import serializers
from .models import StreamEntry

class StreamEntrySerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source='song.artist')
    song = serializers.CharField(source='song.song')

    class Meta:
        model = StreamEntry
        fields = ('date', 'artist', 'song')
