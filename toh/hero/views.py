from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from .models import Hero
from json.decoder import JSONDecodeError
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [{"id": hero.id, "name":hero.name, "age": str(hero.age)} for hero in Hero.objects.all()]
        return JsonResponse(hero_all_list, safe = False)

    elif request.method == "POST":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {"id": hero.id, "name": hero_name}
        return JsonResponse(response_dict, status = 201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

def hero_id(request, id):
    return HttpResponse(f'Your id is {id}!')

def hero_name(request, name=''):
    return HttpResponse(f'Your name is {name}!')

@csrf_exempt
def hero_info(request, id):
    hero = Hero.objects.get(id=id)
    if request.method =="GET":
        hero = Hero.objects.get(id=id)
        response_dict = {"id": hero.id, "name": hero.name, "age": str(hero.age)}
        return JsonResponse(response_dict, safe=False)
    elif request.method =="PUT":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
            hero_age = json.loads(body)["age"]
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {"id": hero.id, "name":hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "PUT"])
        