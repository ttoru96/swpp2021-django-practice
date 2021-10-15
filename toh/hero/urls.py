from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('<int:id>/', views.hero_id),
    path('<str:name>/', views.hero_name),
    path('info/<int:id>/', views.hero_info)
]