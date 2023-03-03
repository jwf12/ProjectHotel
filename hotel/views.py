from django.shortcuts import render
from django.views import generic
from .models import Passanger, Room, Reservation

#  Random id reservation: numbershortuuid.ShortUUID().random(length=6) 

class Home(generic.ListView):
    model = Room
    template_name = 'index.html'
    context_object_name = 'rooms'