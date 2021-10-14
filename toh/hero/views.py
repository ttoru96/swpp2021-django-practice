import json
from json.decoder import JSONDecodeError

from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    JsonResponse,
)
from django.views.decorators.csrf import csrf_exempt

from .models import Hero

# Create your views here.


@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        try:
            body = request.body.decode()
            body = json.loads(body)
            hero_name = body["name"]
            hero_age = body["age"]
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def hero_info(request, id_: int):
    if request.method != "GET" and request.method != "PUT":
        return HttpResponseNotAllowed(["GET", "PUT"])

    try:
        hero = Hero.objects.get(id=id_)
    except Hero.DoesNotExist:
        return HttpResponseBadRequest()

    if request.method == "GET":
        return JsonResponse(hero.to_dict())
    elif request.method == "PUT":
        try:
            body = request.body.decode()
            body = json.loads(body)
            hero_name = body["name"]
            hero_age = body["age"]
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        return JsonResponse(hero.to_dict())


def hero_id(request, id_: int):
    return HttpResponse(f"Your id is {id_}!")


def hero_name(request, name: str):
    return HttpResponse(f"Your name is {name}!")
