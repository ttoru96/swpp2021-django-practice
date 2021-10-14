from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero


# Create your views here.
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


@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        return JsonResponse({'id' : hero.id, 'name' : hero.name, 'age' : hero.age}, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            print(type(body))
            hero_modify = json.loads(body)
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        print(hero_modify)
        hero = Hero.objects.get(id=id)
        hero.name = hero_modify['name']
        hero.age = hero_modify['age']
        hero.save()
        return JsonResponse({'id' : hero.id, 'name' : hero.name, 'age' : hero.age}, safe=False)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])
