##mysite/mysite/polls/views.py

from django.shortcuts import render

# Create your views here.
##nahrany kod tento preda urls polls a to to zas preda urls mysite...OMG
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")