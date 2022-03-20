from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Question, Choice

class List(generic.ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

class Details(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

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
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

class Results(generic.DetailView):
    model = Question
    template_name = "polls/results.html"