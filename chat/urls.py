from django.urls import path

from . import views

urlpatterns = [
    path('', views.registr, name='reg'),
    path('chat/<str:username>', views.index, name='index'),
    path('chat/group/<str:username>/<str:room_name>', views.room, name='room'),
]
