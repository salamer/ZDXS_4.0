from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("hello world")
