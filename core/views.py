from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.]

def hello(request):
    return HttpResponse("Hello World!")

def sum_2number(request):
    return HttpResponse("<h1>This is a test from here</h1>")

