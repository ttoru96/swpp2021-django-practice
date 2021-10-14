from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>', views.hero_info),
    path('<int:id>', views.test_index),
    path('<str:name>', views.test_string),
    ]