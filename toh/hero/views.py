from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

def hero_id(request, id):
  return HttpResponse("Your id is %d" %id)

def hero_name(request, name):
  return HttpResponse("Your name is %s" %name)
@csrf_exempt
def hero_info(request, id):
  if request.method == 'GET':
    id_hero = Hero.objects.get(id=id)
    return JsonResponse(model_to_dict(id_hero))
  elif request.method == 'PUT':
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']
      hero = get_object_or_404(Hero, pk=id)
      #hero = Hero(name=hero_name, age=hero_age)
      hero.age = hero_age
      hero.name = hero_name
      hero.save()
      response_dict = {'id': hero.id, 'name': hero.name, 'age':hero_age}
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'POST'])

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
          response_dict = {'id': hero.id, 'name': hero.name}
          return JsonResponse(response_dict, status=201)
    else:
          return HttpResponseNotAllowed(['GET', 'POST'])