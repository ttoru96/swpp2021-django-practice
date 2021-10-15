from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info),
    path('<int:id>/', views.read_id, name='read_id'),
    path('<str:name>/', views.read_name, name='read_name'),
]