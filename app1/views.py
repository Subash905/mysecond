from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sudeepta(request):
    return HttpResponse('<marquee><h2>Congratulations You are Selected</h2></marquee>')
def raja(request):
    return HttpResponse('I want Job')
    
