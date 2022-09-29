from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    return render(request, 'PBMConsent/index.html')


def pbmquestions(request):
    questions = Question.objects.order_by('question_number')
    context = {'questions': questions}
    return render(request, 'PBMConsent/pbmquestions.html', context)


def consent(request):
    context = {}
    for i, q in enumerate(Question.objects.order_by('question_number')):
        context['answer' + str(i+1)] = request.POST[str(q)]
    return render(request, 'PBMConsent/pbmconsent.html', context)
