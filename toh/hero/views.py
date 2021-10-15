from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json 
from json.decoder import JSONDecodeError
from .models import Hero
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id = 0):
    if request.method == 'GET':
        hero = Hero.objects.get(id = id)
        response_dict = {'id': hero.id, 'name': hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id = id)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {'id': id, 'name': hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)


def id(request, id=0):
    return HttpResponse("Your id is {}!".format(id))

def hero_name(request, name=""):
    return HttpResponse("Your name is {}!".format(name))
