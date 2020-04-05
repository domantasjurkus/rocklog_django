import base64
from datetime import datetime

from django.contrib.auth import authenticate

SUFFIX = '(Klasikinio Roko Legendos)'


def is_authenticated_by_uploading_account(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth_type, b64_payload = request.META['HTTP_AUTHORIZATION'].split()
        if auth_type and b64_payload:
            if auth_type == "Basic":
                byt_decoded = base64.b64decode(b64_payload)
                str_decoded = byt_decoded.decode("utf-8") 
                uname, passwd = str_decoded.split(':')
                user = authenticate(username=uname, password=passwd)
                # not sure if need is_active
                if user is not None and user.is_active:
                    # request.user = user
                    # return view(request, *args, **kwargs)
                    return True
    return False


def extact_song_from_upload(b64_payload):
    data = base64.b64decode(b64_payload)
    data = data.decode("utf-8") 
    artist, song, date, hour = data.split('\n')

    artist = capitalize_artist(artist)
    song = strip_suffix(song)

    return artist, song, date, hour


def capitalize_artist(artist):
    return " ".join(w.capitalize() for w in artist.lower().split())


def strip_suffix(song):
    return song.split(SUFFIX)[0]


def format_entry_date(date, hour):
    datetime_str = " ".join([date, hour])

    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')