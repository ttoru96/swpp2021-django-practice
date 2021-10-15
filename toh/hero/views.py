from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
            hero_age = json.loads(body)["age"]
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name = hero_name, age=hero_age)
        hero.save()
        response_dict = {"id":hero.id, "name":hero.name, "age":hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

def hero_id(request, id):
    return HttpResponse("Your id is {id}".format(id=id))

def hero_name(request, name=""):
    return HttpResponse("Your name is {name}".format(name=name))

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero_selected_info = Hero.objects.filter(id=id).values()[0]
        return JsonResponse(hero_selected_info, safe=False)
    elif request.method =='PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
            hero_age = json.loads(body)["age"]
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id=id)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {"id":hero.id, "name":hero.name, "age":hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "PUT"])
            