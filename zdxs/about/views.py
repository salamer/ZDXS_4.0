from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
	return render(request,"about_index.html")

def website(request):
	return render(request,"about_website.html")