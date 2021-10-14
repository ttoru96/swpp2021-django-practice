from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

def index(request):
    return HttpResponse('Hello, World!')

def id(request, id=0):
    return HttpResponse("Your id is {}!".format(id))

def name(request, name=""):
    return HttpResponse("Your name is {}!".format(name))

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [{'id': hero.id, 'name': hero.name, 'age': str(hero.age)} for hero in Hero.objects.all()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id' : hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=1):
    if request.method == 'GET':
        try:
            hero = Hero.objects.get(id=id)
        except (DoesNotExist, MultipleObjectsReturned) as e:
            return HttpResponseBadRequest()
        result = {'id': hero.id, 'name': hero.name, 'age': str(hero.age)}
        return JsonResponse(result, safe=False)
    elif request.method =='PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        try:
            hero = Hero.objects.get(id=id)
        except (DoesNotExist, MultipleObjectsReturned) as e:
            return HttpResponseBadRequest()
        hero.name = hero_name
        hero.age = int(hero_age)
        hero.save()
        result = {'id': hero.id, 'name': hero.name, 'age': str(hero.age)}
        return JsonResponse(result, safe=False)
    else:
        return HttpResponseNotAllowed(['GET', PUT])