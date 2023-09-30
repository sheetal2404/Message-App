from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Room, Message
from django.utils.text import slugify

from .forms import RoomCreateForm

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomCreateForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)  # Create room object without saving it yet
            room.slug = slugify(room.name)  # Generate slug based on room name
            room.save()  # Save the room object with the generated slug
            return redirect('room', slug=room.slug)  
    else:
        form = RoomCreateForm()
    return render(request, 'room/create_room.html', {'form': form})