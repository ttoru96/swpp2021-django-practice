from django.http import HttpResponse

def hero_id(request, id=""):
    return HttpResponse(f'Your id is {id}!')

def hero_name(request, name=""):
    return HttpResponse(f'Your name is {name}!')