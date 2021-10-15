from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

DEFAULT_AGE = 25
DEFAULT_SCORE = 0

def hero_name(request, name=""):
    return HttpResponse('Your name is {}!'.format(name))

def hero_id(request, id=0):
    return HttpResponse('Your id is {}!'.format(str(id)))

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        for hero in hero_all_list:
            hero['age'] = str(hero['age'])
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            if json.loads(body).get('age') is None:
                hero_age = DEFAULT_AGE
            else:
                hero_age = json.loads(body)['age']
            
            if json.loads(body).get('score') is None:
                hero_score = DEFAULT_SCORE
            else:
                hero_score = json.loads(body)['score']

        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age, score=hero_score)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': str(hero.age), 'score': hero.score}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST']) 

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        response_dict = {'id': hero.id, 'name': hero.name, 'age': str(hero.age), 'score': hero.score}
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero_score = json.loads(body)['score']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id=id)
        hero.name = hero_name
        hero.age = int(hero_age)
        hero.score = hero_score
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': str(hero.age), 'score': hero.score}
        return JsonResponse(response_dict, status=200)
    else:
        return HttpResponseNotAllowed(['GET', 'POST']) 