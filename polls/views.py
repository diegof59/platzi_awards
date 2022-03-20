from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

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
    pass