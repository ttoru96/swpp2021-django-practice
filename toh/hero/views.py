from django.db.models.expressions import F
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse, response
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
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero_age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=0):
    if request.method == 'GET':
        filtered_hero_info = [hero for hero in Hero.objects.filter(id=id).values()]
        return JsonResponse(filtered_hero_info, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
            hero_age = json.loads(body)["age"]
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        target_hero = Hero.objects.get(id=id)
        target_hero.name = hero_name
        target_hero.age = hero_age
        target_hero.save()
        response_dict = {'id': id, 'name': hero_name, 'age': hero_age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])   


# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world")

#def hero_name(request, name=""):
#    return HttpResponse('Your name is ' + name + '!')

#def hero_id(request, id=0):
#    return HttpResponse('Your id is ' + str(id) + '!')
