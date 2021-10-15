import json
from json.decoder import JSONDecodeError
from django.http.response import HttpResponseBadRequest, HttpResponseBase, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from hero.models import Hero
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
  filtered_list = [hero for hero in Hero.objects.filter(age=25).values()]
  return JsonResponse(filtered_list, safe=False)
  # pass

def hero_name(request, name=""):
  return HttpResponse('Your name is {}!'.format(name))

def hero_id(request, id=0):
  return HttpResponse('Your id is {}!'.format(id))

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
    response_dict = {'id': hero_id, 'name': hero.name, 'age': str(hero.age)}
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=0):
  if request.method == 'GET':
    hero = Hero.objects.filter(pk=id).values()[0]
    return JsonResponse(hero, safe=False)
  elif request.method == 'PUT':
    try:
      body = request.body.decode()
      info = json.loads(body)
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    hero = Hero.objects.filter(pk=id)
    hero.name = info['name']
    hero.age = int(info['age'])
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'age': str(hero.age)}
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'PUT'])