from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.]

def hello(request):
    return HttpResponse("Hello World!")


def sum_2number(request):
    return HttpResponse("This is a test from here")

