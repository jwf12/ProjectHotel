from hotel.models import Reservation, Room, Passanger
from caja.models import *
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from datetime import date
from hotel.filters import SearchFilter
from django.contrib import messages
from django.db.models import Sum


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
    till = Till.objects.get(till_res=reservation)

    #se crea la variable para los items de determinada reserva
    items = Item_Till.objects.filter(item_till=till)
    #se crea la variable para los pagos de determinada reserva
    payments = Payment.objects.filter(payment_till=till)

    # Sumar los montos de los items
    total_amount_items = items.aggregate(Sum('price'))['price__sum'] or 0
    # Sumar los montos de las transacciones de pago
    total_amount_pays = payments.aggregate(Sum('amount'))['amount__sum'] or 0
    #la diferencia entre los 2
    total_total =  total_amount_items + total_amount_pays
    
    if (total_total == 0):
        reservation.status_res = 3
        reservation.save()
        messages.success(request, 'Reservation check-out')
        return HttpResponseRedirect(reverse_lazy('hotel:home'))
    else:
        messages.error(request, f'This reservation has charges to pay - ${total_total}')
        return HttpResponseRedirect(reverse_lazy('hotel:home'))



#Status buttons used in rooms.html
def room_clean(request, pk):
    room = Room.objects.get(pk=pk)
    room.status = '#9bf0ac'
    room.save()
    return HttpResponseRedirect(reverse_lazy('hotel:room'))

#Status buttons used in rooms.html
def room_blocked(request, pk):
    room = Room.objects.get(pk=pk)
    room.status = '#D47777'
    room.save()
    return HttpResponseRedirect(reverse_lazy('hotel:room'))

#Status buttons used in rooms.html
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

#Check in button in search
def check_in(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if reservation.room.state == 2:
        messages.error(request, 'Occupied room')
        return HttpResponseRedirect(reverse_lazy('hotel:search'))
    reservation.status_res = 2
    reservation.save()
    messages.success(request, 'Reservation check-in')
    return HttpResponseRedirect(reverse_lazy('hotel:home'))

#No-Show button in search
def no_show(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.status_res = 4
    reservation.save()
    messages.success(request, 'Reservation No-show')
    return HttpResponseRedirect(reverse_lazy('hotel:search'))


#Search View filter
def searchView(request):
    reservation = Reservation.objects.all()    
    myFilter = SearchFilter(request.GET, queryset=reservation)
    reservation = myFilter.qs
    room = Room.objects.all()
    passangers=Passanger.objects.all()
    till = Till.objects.all()
    
    return render(request, 'search.html', context={
                                                    'myFilter':myFilter,
                                                    'reservations':reservation,
                                                    'rooms':room,
                                                    'passangers':passangers,
                                                    'tills': till,
                                                    })