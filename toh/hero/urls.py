from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.hero_id),
    path('<str:name>/', views.hero_name)
]
