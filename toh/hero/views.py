import json
from json.decoder import JSONDecodeError

from django.db.models import Model
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from hero.models import Hero


def index(request):
    return HttpResponse('Hello, world!')


@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    if request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def hero_info(request, hero_id=0):
    if request.method == 'GET':
        try:
            hero_get = Hero.objects.get(id=hero_id)
        except Model.DoesNotExist:
            return HttpResponseBadRequest()
        response_dict = {'id': hero_get.id, 'name': hero_get.name, 'age': hero_get.age}
        return JsonResponse(response_dict, status=200)
    if request.method == 'PUT':
        try:
            hero_target = Hero.objects.get(id=hero_id)
        except Model.DoesNotExist:
            return HttpResponseBadRequest()

        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()

        hero_target.name = hero_name
        hero_target.age = hero_age
        hero_target.save()
        response_dict = {'id': hero_target.id, 'name': hero_target.name, 'age': hero_target.age}
        return JsonResponse(response_dict, status=200)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])


def hero_name(request, hero_name=""):
    return HttpResponse('Your name is ' + hero_name + '!')


def hero_id(request, hero_id=0):
    return HttpResponse('Your id is ' + str(hero_id) + '!')
