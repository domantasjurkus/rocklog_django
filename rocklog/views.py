from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth

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
    saved_songs = SavedSong.objects.all().filter(user=user_id)
    context = {
        'header_link_text': 'Visos dainos',
        'header_link_url': '/',
        'stream': decorate_with_saved_all(saved_songs),
    }
    return render(request, 'rocklog/index.html', context)


# @login_required
# def home(request):
#     return render(request, 'rocklog/index.html')

def hamster_logout(request):
    return HttpResponse('hamster_logout')


def videoid(request, artist, song):
    return HttpResponse(getYoutubeId(artist, song))

    # def detail(request, question_id):
    #     # try:
    #     #     question = Question.objects.get(pk=question_id)
    #     # except Question.DoesNotExist:
    #     #     raise Http404("Question does not exist")
    #     question = get_object_or_404(Question, pk=question_id)
    #     return render(request, 'polls/detail.html', {'question': question})

    #         """
    #         Excludes any questions that aren't published yet.
    #         """
    #         return Question.objects.filter(date__lte=timezone.now())

    # def results(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     return render(request, 'polls/results.html', {'question': question})

    # class ResultsView(generic.DetailView):
    #     model = Question
    #     template_name = 'polls/results.html'

    # def vote(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     # what if the selected choice does not exist?
    #     try:
    #         # question.choice_set gets auto-generated since Choice has a foreign key to Question
    #         selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #     except (KeyError, Choice.DoesNotExist):
    #         # Redisplay the question voting form.
    #         return render(request, 'polls/detail.html', {
    #             'question': question,
    #             'error_message': "You didn't select a choice.",
    #         })
    #     else:
    #         selected_choice.votes += 1
    #         selected_choice.save()
    #         # Always return an HttpResponseRedirect after successfully dealing
    #         # with POST data. This prevents data from being posted twice if a
    #         # user hits the Back button.

    #         # why do we reverse?
    #         return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))
