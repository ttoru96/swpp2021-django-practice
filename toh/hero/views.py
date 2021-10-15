from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero
# Create your views here.

def index(request):
    return HttpResponse('Hello, world!')

def hero_id(request, id):
    return HttpResponse(f'Your id is {id}!')

def hero_name(request, name=""):
    return HttpResponse(f'Your name is {name}!')

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id' : hero.id, 'name' : hero.name, 'age' : hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    hero = get_object_or_404(Hero, id=id)
    if request.method == 'GET':
        response_dict = {'id' : hero.id, 'name' : hero.name, 'age' : hero.age}
        return JsonResponse(response_dict, status=200)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero.name = hero_name
        hero.age = hero_age
        print("debug" + hero_age)
        hero.save()
        response_dict = {'id' : hero.id, 'name' : hero.name, 'age' : hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    return JsonResponse(hero_all_list, safe = False)
