from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stats', views.stats, name='stats'),
    path('health', views.health, name='health'),
    path('update', views.update, name='update')
]