from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from rocklog.models import StreamSong


def index(request):
    stream = StreamSong.objects.all().order_by('-id')[:15]
    context = {
        'stream': stream
    }
    return render(request, 'rocklog/index.html', context)


def videoid(request, artist, song):

    return HttpResponse("You're looking at %s - %s" % (artist, song))

    # def detail(request, question_id):
    #     # try:
    #     #     question = Question.objects.get(pk=question_id)
    #     # except Question.DoesNotExist:
    #     #     raise Http404("Question does not exist")
    #     question = get_object_or_404(Question, pk=question_id)
    #     return render(request, 'polls/detail.html', {'question': question})

    # class DetailView(generic.DetailView):
    #     model = Question
    #     template_name = 'polls/detail.html'

    #     def get_queryset(self):
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
