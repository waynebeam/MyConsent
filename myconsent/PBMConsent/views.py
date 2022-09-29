from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    return render(request, 'PBMConsent/index.html')


def pbmquestions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'PBMConsent/pbmquestions.html', context)
