from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.template import loader
import logging

logger = logging.getLogger(__name__)

def index(request):
    try:
        num = 1/0
    except:
        logger.exception("Exception was caught!")

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # return HttpResponse("Hello world!")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)