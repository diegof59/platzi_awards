from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Question, Choice

class List(generic.ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name = "question_list"

    def get_queryset(self):
        return Question.objects.filter(publication_date__lte=timezone.now()).order_by("-publication_date")

class Details(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        return Question.objects.filter(publication_date__lte=timezone.now())

def vote(request, question_id:int):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_msg":"No elegiste una respuesta."
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse_lazy("polls:results", args=(question.id,)))

class Results(generic.DetailView):
    model = Question
    template_name = "polls/results.html"