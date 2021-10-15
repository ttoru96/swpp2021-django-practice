import json
from json.decoder import JSONDecodeError
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from hero.models import Hero
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def hero_id(request, id=""):
    return HttpResponse(f"Your name is {id}!")

def hero_name(request, name=""):
    return HttpResponse(f"Your name is {name}!")

@csrf_exempt
def hero_info(request, id=""):
    if request.method =="GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        selectedHero = None
        for hero in hero_all_list:
            if hero['id']==id:
                selectedHero = hero
        return JsonResponse(selectedHero, safe=False)
    elif request.method == "PUT":
        body = request.body.decode()
        hero_name = json.loads(body)['name']
        hero_age = json.loads(body)['age']
        
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        selectID = -1
        for hero in hero_all_list:
            if hero['id']==id:
                selectID=id
        if selectID!=-1:
            editHero = get_object_or_404(Hero, pk=selectID)
            editHero.age = hero_age
            editHero.save()
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(["GET", "PUT"])

@csrf_exempt
def hero_list(request):
    if request.method=="GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name = hero_name, age=hero_age)
        hero.save()

        response_dict = {'id': hero.id, 'name':hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else: 
        return HttpResponseNotAllowed(["GET", "POST"])
