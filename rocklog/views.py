import base64

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from rocklog.models import Song, StreamEntry, SavedSong
from rocklog.controllers.youtube import getYoutubeId


def decorate_with_saved_all(stream):
    for stream_entry in stream:
        stream_entry.saved = True
    return stream


def decorate_with_saved_user(stream, saved_songs):
    for entry in stream:
        for saved_song in saved_songs:
            if entry.song_id == saved_song.song_id:
                entry.saved = True
    return stream

def index(request):
    stream = StreamEntry.objects.select_related('song').order_by('-date')[:15]
    stream = stream.select_related('song')

    if request.user.id:
        saved_songs = SavedSong.objects.filter(user_id=request.user.id).select_related('song')
        stream = decorate_with_saved_user(stream, saved_songs)

    context = {
        'header_link_text': 'Išsaugotos dainos',
        'header_link_url': 'saved',
        'stream': stream
    }
    return render(request, 'rocklog/index.html', context)


@login_required
def saved_songs(request):
    user_id = request.user.id
    saved_songs = SavedSong.objects.filter(user=user_id)
    context = {
        'header_link_text': 'Visos dainos',
        'header_link_url': '/',
        'stream': decorate_with_saved_all(saved_songs),
    }
    return render(request, 'rocklog/index.html', context)


@login_required
def toggle_save(request, song_id):
    user_id = request.user.id

    saved_song = SavedSong.objects.filter(user_id=user_id).filter(song_id=song_id)
    is_song_saved = len(saved_song) > 0
    
    if (is_song_saved):
        saved_song.delete()
    else:
        s = SavedSong(song_id=song_id, user_id=user_id)
        s.save()

    return HttpResponse('song saved/removed')


def videoid(request, artist, song):
    return HttpResponse(getYoutubeId(artist, song))


def is_authenticated_by_uploading_account(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).split(':')
                user = authenticate(username=uname, password=passwd)
                # not sure if need is_active
                if user is not None and user.is_active:
                    # request.user = user
                    # return view(request, *args, **kwargs)
                    return True
    return False


def upload_new_song(request, payload):
    if !is_authenticated_by_uploading_account(request):
        return HttpResponseForbidden()

    data = base64.b64decode(payload)
    data = data.decode("utf-8") 
    artist, song, date, hour = data.split('\n')

    print(request.META['HTTP_AUTHORIZATION'])
    
    # TODO: PascalCase Artist
    print()
    print(artist)
    print(song)
    print(date)
    print(hour)
    print()



    return HttpResponse('new song uploaded')


    # raise http404 error
    # question = get_object_or_404(Question, pk=question_id)

    # # question.choice_set gets auto-generated since Choice has a foreign key to Question
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # # Always return an HttpResponseRedirect after successfully dealing
    # # with POST data. This prevents data from being posted twice if a
    # # user hits the Back button.
    # return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))
