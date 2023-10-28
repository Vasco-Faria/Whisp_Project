from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Room


@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    
    return render(request,'room/rooms.html',{'rooms': rooms})


@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    
    return render(request,'room/room.html',{'room': room})