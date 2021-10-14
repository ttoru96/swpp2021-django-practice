from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json.decoder import JSONDecodeError
from .models import Hero
import json


def index(request):
    return HttpResponse('Hello, world!')


def read_id(request, id):
    return HttpResponse(f'Your id is {id}!\n')


def read_name(request, name):
    return HttpResponse(f'Your name is {name}!\n')


@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()  # default decoder : UTF-8
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id=id)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        print(hero)
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
