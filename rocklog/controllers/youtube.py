# import urllib.parse
from django.conf import settings
import urllib.request
from urllib.parse import urlencode, quote_plus
import json

import requests


def unnest_id(requests_response):
    return requests_response.json()['items'][0]['id']['videoId']


def getYoutubeId(artist, song):
    params = urlencode({
        'key': settings.YOUTUBE_API_KEY,
        'maxResults': 1,
        'part': 'id',
        'q': quote_plus(f'{artist} {song}'),
        'fields': 'items(id/videoId)',
    })

    url = f'https://content.googleapis.com/youtube/v3/search?{params}'

    return unnest_id(requests.get(url))
