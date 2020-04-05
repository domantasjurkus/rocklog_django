from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from rocklog.models import Song, StreamEntry, SavedSong
from rocklog.controllers.youtube import getYoutubeId

from .utils.saved import decorate_with_saved_all, decorate_with_saved_user
from .utils.upload import extact_song_from_upload, is_authenticated_by_uploading_account, capitalize_artist

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
    is_song_saved_already = len(saved_song) > 0
    
    if (is_song_saved_already):
        saved_song.delete()
    else:
        s = SavedSong(song_id=song_id, user_id=user_id)
        s.save()

    return HttpResponse('song saved/removed')


def videoid(request, artist, song):
    return HttpResponse(getYoutubeId(artist, song))


def upload_new_song(request, b64_payload):
    if not is_authenticated_by_uploading_account(request):
        return HttpResponseForbidden()

    artist, song_name, date, hour = extact_song_from_upload(b64_payload)

    song = Song.get(artist, song_name).first()

    if not song:
        song = Song(artist=artist, song=song_name)
        song.save()

    if StreamEntry.is_latest_entry_already_added(song):
        return HttpResponse('entry already uploaded - nothing to do')

    entry = StreamEntry(song=song)
    entry.save()

    return HttpResponse('new song entry uploaded')


    # raise http404 error
    # question = get_object_or_404(Question, pk=question_id)

    # # question.choice_set gets auto-generated since Choice has a foreign key to Question
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # # Always return an HttpResponseRedirect after successfully dealing
    # # with POST data. This prevents data from being posted twice if a
    # # user hits the Back button.
    # return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))
