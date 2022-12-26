from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def subash(request):
    return HttpResponse('<marquee><h2>Congratulations You Win 5000</h2></marquee>')
    