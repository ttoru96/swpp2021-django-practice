from django.urls import path
from . import views

urlpatterns = [
  path('', views.hero_list),
  path('<int:num>/', views.numbering),
  path('<str:name>/', views.naming),
  path('info/<int:target_id>/', views.hero_info),
]