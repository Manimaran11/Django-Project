from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
     return HttpResponse("hello,World, YOu are at polls index")