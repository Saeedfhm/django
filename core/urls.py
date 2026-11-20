from core.views import *
from django.urls import path

urlpatterns = [
    path("" , home),
    path("about" , about),
    path("contact" , contact)
]