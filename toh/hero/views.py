from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

def index(request):
  return HttpResponse('Hello, world!')

def hero_id(request, id=0):
  return HttpResponse(f'Your id is {id}!')

def hero_name(request, name=""):
  return HttpResponse(f'Your name is {name}!')

@csrf_exempt
def hero_list(request):
  if request.method == 'GET':
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    for hero in hero_all_list:
      hero['age'] = str(hero['age'])
      hero['score'] = str(hero['score'])
    return JsonResponse(hero_all_list, safe=False)
  elif request.method == 'POST':
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.load(body)['age']
      hero_score = json.loads(body)['score']
    except (KeyError, JSONDecodeError):
      return HttpResponseBadRequest()
    hero = Hero(name=hero_name, age=hero_age, score=hero_score)
    hero.save()
    response_dict = { 'id':hero.id, 'name': hero.name, 'age': str(hero.age), 'score': str(hero.score) }
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['Get', 'POST', ])

@csrf_exempt
def hero_info(request, id=0):
  if request.method == 'GET':
    hero_select_list = [hero for hero in Hero.objects.filter(id=id).values()]
    try:
      print(type(hero_select_list[0]))
      hero_select_list[0]['age'] = str(hero_select_list[0]['age'])
      hero_select_list[0]['score'] = str(hero_select_list[0]['score'])
      return JsonResponse(hero_select_list[0], status=200)
    except IndexError:
      return JsonResponse(None, status=200)
  elif request.method == 'PUT':
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']
      hero_score = json.loads(body)['score']
    except (KeyError, JSONDecodeError):
      return HttpResponseBadRequest()
    try:
      hero = Hero.objects.get(id=id)
      hero.name = hero_name
      hero.age = hero_age
      hero.score = hero_score
      hero.save()
      response_dict = { 'id': hero.id, 'name': hero_name, 'age':hero_age, 'score':hero_score }
      return JsonResponse(response_dict, status=201)
    except:
      return JsonResponse(None, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'PUT', ])