from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chattwpn.models import Message, Room, User


# Create your views here.
def index(request):
    return render(request, 'chattwpn/index.html')


def home(request):
    return render(request, 'chattwpn/home.html')


def room(request, room):
    username = request.GET.get('username')
    room_name = Room.objects.get(name=room)
    return render(request, 'chattwpn/room.html', {
        'username':username,
        'room':room,
        'room_name':room_name,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    email = request.POST['email']
    number = request.POST['contact']

    if Room.objects.filter(name=room).exists():
        user = User.objects.create(username=username, room=room, number=number, email=email)
        user.save()
        return redirect(''+room+'/?username='+username)

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        user = User.objects.create(username=username, room=room, number=number, email=email)
        user.save()
        return redirect(''+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(values=message, username=username, room=room_id)
    new_message.save()
    return HttpResponse("Message Sent Successfully!")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    message = Message.objects.filter(room=room_details.id)
    return JsonResponse({"contents":list(message.values())})