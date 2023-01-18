from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Assalamu")

# Create your views here.
