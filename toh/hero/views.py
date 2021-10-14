from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

def index(request):
    return HttpResponse('Hello, world!')

def hero_name(request, name=""):
    return HttpResponse('Your name is ' + name + "!")

def hero_id(request, id=0):
    return HttpResponse('Your id is ' + str(id) + "!")

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['Get', 'POST'])
    
@csrf_exempt
def hero_info(request, id=0):
    if request.method == 'GET':
        selected_hero = Hero.objects.get(id=id)
        response_dict = {
            'id': selected_hero.id,
            'name': selected_hero.name,
            'age': selected_hero.age,
        }
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        selected_hero = Hero.objects.get(id=id)
        selected_hero.name = hero_name
        selected_hero.age = age
        selected_hero.save()
        response_dict = {'id': id, 'name': selected_hero.name, 'age': selected_hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['Get', 'POST'])
# Create your views here.
