from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from json.decoder import JSONDecodeError
from .models import Hero 


def index(request):
    return HttpResponse('Hello, world!')

def heroId(request, id=""):
    return HttpResponse("Your id is {}".format(id))

def heroName(request, name=""):
    return HttpResponse("Your name is {}".format(name))

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
def hero_info(request, id=""):
    hero = Hero.objects.filter(id=id)
    if request.method == 'GET':
        if hero.exists():
            return JsonResponse(hero.values()[0])
        else:
            return HttpResponseBadRequest()
    elif request.method == 'PUT':
        hero = hero[0]
        try: 
            body = request.body.decode() 
            hero_name = json.loads(body)['name'] 
            hero_age = json.loads(body)['age'] 
        except (KeyError, JSONDecodeError) as e: 
            return HttpResponseBadRequest() 
        hero.age = hero_age
        hero.name = hero_name 
        hero.save() 
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age} 
        return JsonResponse(response_dict, status=201) 
    else: 
        return HttpResponseNotAllowed(['GET', 'POST'])