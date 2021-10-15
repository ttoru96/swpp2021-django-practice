from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info, name="hero_info"),
    path('<int:id>/', views.hero_id, name='hero_id'),
    path('<str:name>/', views.hero_name, name='hero_name'),
]