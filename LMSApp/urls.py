from django.urls import path
from .views import index, team
urlpatterns = [
    path('', index, name='index'),
    path('', team, name='team'),
]