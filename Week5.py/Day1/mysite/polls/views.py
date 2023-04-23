from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def index(request):
    context ={'weather':'warm',}
    return render(request, 'index.html', context)
# Create your views here

def about(request):
    return HttpResponse('<h1> Welcome Users<h1>','<h2>This is about website page<\h2>')
