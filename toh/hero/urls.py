from django.urls import path

from . import views

urlpatterns = [
    path('info/<int:id>/', views.hero_info, name='info'),
    path('', views.hero_list, name='index'),
    path('<int:id>/', views.hero_id, name='id'),
    path('<slug:name>/', views.hero_name, name='name'),
]
