from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

def list(request):
    latest_question_list = Question.objects.all()
    return render(
        request,
        "polls/index.html",
        {"latest_question_list": latest_question_list}
    )

def details(request, question_id:int):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/details.html",
        {"question": question}
    )

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

def results(request, question_id:int):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/results.html",
        { "question": question}
    )