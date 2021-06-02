from django.shortcuts import render

from .models import Message

def index(request, username):
    username = username
    return render(request, 'chat/index.html', {'username': username})


def room(request, room_name, username):
    username = username
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})

def registr(request):
    return render (request, 'chat/registr.html')
