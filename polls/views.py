from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def details(request, question_id):
    try:
        question = Question.objects.get(pk= question_id)
    except Question.DoesNotExist:
        raise Http404("Question does't exist")
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    response = "You are looking at the result of question %s ."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're responding to vote %s" % question_id)
