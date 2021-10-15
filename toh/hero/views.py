from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

def hero_id(request, id=1):
    return HttpResponse('Your name is %d!' % id)

def hero_name(request, name=""):
    return HttpResponse('Your name is %s!' % name)

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
        response_dict = {'id': hero.id, 'name': hero.name, 'age':str(hero.age)}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    hero = Hero.objects.get(id=id)
    if request.method == "GET":
        response_dict = {'id': hero.id, 'name': hero.name, 'age':str(hero.age)}
        return JsonResponse(response_dict, safe=False)
    elif request.method == "PUT":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age':str(hero.age)}
        return JsonResponse(response_dict, safe=False)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])

# def index(request):
#     return HttpResponse("Hello, world")

