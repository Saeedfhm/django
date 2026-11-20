from django.test import TestCase
from django.http import HttpResponse


def run_title(request):
    return HttpResponse("test.py page")

