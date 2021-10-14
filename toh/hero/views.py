from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero


# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')


def hero_name(request, name=""):
    return HttpResponse('Your name is ' + name + '!')


def hero_id(request, id=-1):
    return HttpResponse('Your id is ' + str(id) + '!')
