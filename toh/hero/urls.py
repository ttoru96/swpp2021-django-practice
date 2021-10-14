from django.urls import path

from . import views

urlpatterns = [
    path("", views.hero_list),
    path("<int:id_>", views.hero_info),
    path("<str:name>", views.hero_name),
]
