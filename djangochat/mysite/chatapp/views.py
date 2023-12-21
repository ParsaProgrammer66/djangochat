from django.shortcuts import render
from .models import Chatroom,ChatMessage
# Create your views here.

def index(request):
    chatrooms=Chatroom.objects.all()
    return render(request,'chatapp/index.html',{'chatrooms':chatrooms})


def chatroom(request,slug):
    chatroom=Chatroom.objects.get(slug=slug)
    messages=ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request,'chatapp/room.html',{'chatroom':chatroom,'messages':messages})