'''
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')
'''

from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

def hero_id(request, id):
    return HttpResponse('Your id is ' + str(id) + '!')

def hero_name(request, name):
    return HttpResponse('Your name is ' + name + '!')

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
def hero_info(request, searchId):
    if request.method == 'GET':
        selected_hero = [hero for hero in Hero.objects.filter(id=searchId).values()]
        return JsonResponse(selected_hero, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id = searchId)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        return JsonResponse({'id' : hero.id, 'name' : hero.name, 'age' : hero.age}, safe=False)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])    
