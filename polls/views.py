# Create your views here.
from django.http import (HttpResponse,
                         HttpResponseRedirect,
                         Http404)
from .models import (Question,
                     Choice)
from django.template import loader
from django.shortcuts import (render,
                              get_object_or_404)
from django.core.urlresolvers import reverse


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
    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/details.html',{
            'question': question,
            'error_message': "You've not selected a choice"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
