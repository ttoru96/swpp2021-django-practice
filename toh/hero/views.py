from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age=json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age':hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def index(request):
    return HttpResponse('Hello, world!')

def hero_id(request, id=''):
    return HttpResponse('Your id is '+str(id)+"!")

def hero_name(request, name=''):
    return HttpResponse('Your name is '+name+"!")

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        search_hero = Hero.objects.get(id=id)
        response_dict = {'id': search_hero.id, 'name': search_hero.name, 'age':search_hero.age}
        return JsonResponse(response_dict, safe=False)
    elif request.method=='PUT':
        search_hero = Hero.objects.get(id=id)
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age=json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        search_hero.name=hero_name
        search_hero.age=hero_age
        search_hero.save()
        response_dict = {'id': search_hero.id, 'name': search_hero.name, 'age':search_hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])