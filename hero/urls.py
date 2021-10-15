from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.id, name='id'),
    path('<str:name>', views.name, name = 'name'),
    path('', views.hero_list),
    path('info/<int:id>', views.hero_info)
]
