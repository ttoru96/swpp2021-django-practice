from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.id_test, name='id_test'),
    path('<str:name>/', views.name_test, name='name_test'),
    
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info)
]