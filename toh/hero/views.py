from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero


# def index(request):
#     return HttpResponse("Hello World!")


# def print_id(request, id=1):
#     return HttpResponse(f"your id is {id}!")


# def print_name(request, name="hi"):
#     return HttpResponse(f"your name is {name}!")


@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
            hero_age = json.loads(body)["age"]
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def hero_info(request, id=1):
    if request.method == "GET":
        try:
            hero = Hero.objects.get(pk=id)
            print(hero)
            response_dict = {id: hero.id, "name": hero.name, "age": hero.age}
        except (KeyError, JSONDecodeError) as e:
            HttpResponseBadRequest()
        else:
            return JsonResponse(response_dict, status=200)
    elif request.method == "PUT":
        try:
            hero = Hero.objects.get(pk=id)
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
            hero_age = json.loads(body)["age"]
            hero.name = hero_name
            hero.age = hero_age
            hero.save()
            response_dict = {id: hero.id, "name": hero.name, "age": hero.age}
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        else:
            return JsonResponse(response_dict, status=200)


# Create your views here.
