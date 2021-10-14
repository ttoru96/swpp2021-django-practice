import json
from json.decoder import JSONDecodeError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse

from hero.models import Hero


def hero_id(request, id: int = 0):
    return HttpResponse('Your id is {}!'.format(id))


def hero_name(request, name: str = 0):
    return HttpResponse('Your name is {}!'.format(name))


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
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def hero_info(request, id: int = 0):
    if request.method == 'GET':
        try:
            hero = Hero.objects.get(id=id)
            response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
            return JsonResponse(response_dict)
        except Hero.DoesNotExist:
            return HttpResponseBadRequest(status=401)

    elif request.method == 'PUT':
        try:
            hero = Hero.objects.get(id=id)
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError, Hero.DoesNotExist):
            return HttpResponseBadRequest(status=401)
        hero.name = hero_name
        hero.age = hero_age
        response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(response_dict)
