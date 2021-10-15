from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info),
    path('<int:id>/', views.heroId),
    path('<str:name>/', views.heroName),
]