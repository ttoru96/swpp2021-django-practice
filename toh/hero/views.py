from django.shortcuts import render
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
                  hero_age = json.loads(body)['age']
            except (KeyError, JSONDecodeError) as e:
                  return HttpResponseBadRequest()
            hero = Hero(name=hero_name, age=hero_age)
            hero.save()
            response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
            return JsonResponse(response_dict, status=201)
      else:
            return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=0):
      if request.method == 'GET':
            hero_all_list = [hero for hero in Hero.objects.all().values()]
            for h in hero_all_list:
                  if h["id"] == id:
                        return JsonResponse(h, safe=False)
            return JsonResponse(None, safe=False)
      elif request.method == 'PUT':
            body = request.body.decode()
            hero = Hero(name=json.loads(body)["name"], age=json.loads(body)["age"])
            newhero = {"id": id, "name": hero.name, "age": hero.age}
            hero.id = id
            hero.save()
            return JsonResponse(newhero, safe=False)
                        
      else:
            return HttpResponseNotAllowed(['GET', 'PUT'])


def index(request):
    return HttpResponse('Hello, world!')

def hero_int(request, id=0):
    return HttpResponse('Your id is ' + str(id) + '!')

def hero_name(request, name=""):
    return HttpResponse('Your name is ' + name + '!')

# Create your views here.
