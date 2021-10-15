from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list),
    path('<int:id>/', views.printInt, name='print_int'),
    path('<str:name>/', views.printString, name='print_string'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
    
]

