from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('info/<int:id>/', views.hero_info)
]
