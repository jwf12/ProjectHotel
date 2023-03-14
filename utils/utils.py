from hotel.models import Reservation, Room
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Funcion para cambiar el estado del room en caso que se le de check in a la reserva.

def room_change_satate():
    reserved_rooms = set(Reservation.objects.filter(status_res=2).values_list('room__id', flat=True))
    all_rooms = Room.objects.all()
    
    for room in all_rooms:
        if room.id in reserved_rooms:
            room.state = 2
        else:
            room.state = 1
        room.save()
    
    return None


def room_checkout(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.status_res = 3
    reservation.save()
    return HttpResponseRedirect(reverse_lazy('hotel:home'))

# def room_checkout(request, pk):
#     reservation = Reservation.objects.filter(pk=pk)
#     reservation.status_res = 3
#     success_url = reverse_lazy('hotel:home')
#     return render(request, 'index.html', context={'reservation': 'reservation',})

