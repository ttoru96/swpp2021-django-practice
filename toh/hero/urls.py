from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.hero_id, name='id'),
    path('<str:name>', views.hero_name, name='name')
]