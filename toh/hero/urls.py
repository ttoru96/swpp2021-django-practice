from django.urls import path

from . import views

urlpatterns = [
  path('<int:id>/', views.hero_id),
  path('info/<int:id>/', views.hero_info),
  path('<str:name>/', views.hero_name),
  path('', views.hero_list),
]