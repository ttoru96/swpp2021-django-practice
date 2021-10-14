from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from json.decoder import JSONDecodeError
from .models import Hero


@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def hero_info(request, id=0):
    if request.method == 'GET':
        try:
            hero_info = Hero.objects.filter(id=id)
            return JsonResponse(hero_info.values()[0], safe=False)
        except:
            return HttpResponseBadRequest()
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero = Hero.objects.get(age=id)
            hero.name = json.loads(body)["name"]
            hero.age = json.loads(body)["age"]
            hero.save()
            response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
            return JsonResponse(response_dict, status=201)
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest(['GET', 'PUT'])


def index(request):
    return HttpResponse('Hello,world!')


def hero_id(request, id=0):
    return HttpResponse('Your id is {}!'.format(id))


def hero_name(request, name=""):
    return HttpResponse('Your name is '+name+'!')

# Create your views here.
