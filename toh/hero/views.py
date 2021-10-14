from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

# Create your views here.

def index(request) :
    return HttpResponse('Hello, world!')

@csrf_exempt
def hero_list(request) :
  if request.method == 'GET' :
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    return JsonResponse(hero_all_list, safe=False)
  
  elif request.method == 'POST' :
    try :
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']
    except (KeyError, JSONDecodeError) as e :
      return HttpResponseBadRequest()
  
    hero = Hero(name=hero_name, age=hero_age)
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, status=201)
  
  else :
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=0) :
  if request.method == 'GET' :
    try :
      hero = Hero.objects.get(id=id)
    except (Hero.DoesNotExist) as e :
      return HttpResponseBadRequest()
    
    response_dict = {'id': hero.id, 'name': hero.name, 'age': str(hero.age)}
    return JsonResponse(response_dict)
  
  elif request.method == 'PUT' :
    try :
      body = request.body.decode()
      new_name = json.loads(body)['name']
      new_age = int(json.loads(body)['age'])
    except (KeyError, ValueError, JSONDecodeError) as e :
      return HttpResponseBadRequest()
    
    try :
      hero = Hero.objects.get(id=id)
    except (Hero.DoesNotExist) as e :
      return HttpResponseBadRequest()
    
    hero.name = new_name
    hero.age = new_age
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'age': str(hero.age)}
    return JsonResponse(response_dict, status=201)
  
  else :
    return HttpResponseNotAllowed(['GET', 'PUT'])

def hero_id(request, id=0) :
  return HttpResponse('Your id is {}!'.format(id))

def hero_name(request, name='') :
  return HttpResponse('Your name is {}!'.format(name))
