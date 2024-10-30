from django.http import HttpResponse
from django.shortcuts import render
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

    return HttpResponse("Hello world!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)