from hotel.models import Reservation, Room
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from datetime import date
from hotel.filters import SearchFilter

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

#function used in index to check out a room
def room_checkout(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.status_res = 3
    reservation.save()
    return HttpResponseRedirect(reverse_lazy('hotel:home'))


#Status buttons used in rooms.html
def room_clean(request, pk):
    room = Room.objects.get(pk=pk)
    room.status = '#9bf0ac'
    room.save()
    return HttpResponseRedirect(reverse_lazy('hotel:room'))


def room_blocked(request, pk):
    room = Room.objects.get(pk=pk)
    room.status = '#D47777'
    room.save()
    return HttpResponseRedirect(reverse_lazy('hotel:room'))


def room_dirty(request, pk):
    room = Room.objects.get(pk=pk)
    room.status = '#fffb8f'
    room.save()
    return HttpResponseRedirect(reverse_lazy('hotel:room'))


def reservations_check(room, date_in, date_out, status_res):
    today = date.today()
    reservation = Reservation.objects.filter(room_id = room, date_in__lte = today, date_out__gte = today, status_res = 1)

    if reservation:
        return 'ya existe'


#Search View
def searchView(request):
    reservation = Reservation.objects.all()    
    myFilter = SearchFilter(request.GET, queryset=reservation)
    reservation = myFilter.qs
    
    return render(request, 'search.html', context={'myFilter':myFilter, 'reservations':reservation})