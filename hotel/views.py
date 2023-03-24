from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Passanger, Room, Reservation
from utils.utils import room_change_satate
from django.shortcuts import get_object_or_404
from datetime import date



class Home(generic.ListView):
    queryset = Room.objects.all().order_by('id')
    template_name = 'index.html'
    context_object_name = 'rooms'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(status_res=2) 
        room_change_satate()   
        return context


class ShowPassData(generic.DetailView):
    model = Passanger
    template_name = 'passanger.html'
    context_object_name = 'passan'


class ShowRooms(generic.ListView):
    queryset = Room.objects.all().order_by('id')
    template_name = 'rooms.html'
    context_object_name = 'rooms'


class RoomEditarView(generic.UpdateView):
    model = Room
    success_url = reverse_lazy('hotel:room')
    fields = [
        'observations',
        ]

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)
    

class PassangerEditarView(generic.UpdateView):
    model = Passanger
    success_url = reverse_lazy('hotel:home')
    fields = [
        'name',
        'dni',
        'tel',
        'country',
        'city',
        'adress',
        'email',
        'birth_date',
        'observations',

    ]

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)


#modify reservation. 
class UpdateReservationView(generic.UpdateView):
    model = Reservation
    success_url = reverse_lazy('hotel:home')
    fields = [
            'room',
            'date_in',
            'date_out',
            'amount_people',
            'observations',
    ]

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)

#Create a reservation.
class CreateReservation(generic.CreateView):
    model = Reservation   
    context_object_name = 'reservations'
    template_name = 'reservation.html'
    success_url = reverse_lazy('hotel:home')    

    fields = [
        'passanger',
        'room',
        'type_res',
        'date_in',
        'date_out',
        'number',
        'amount_people',
        'status_res',
        'observations',
    ]   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        context['passangers'] = Passanger.objects.all()
        context['today'] = date.today()
        return context
    
    def form_valid(self, form):
        # Validating if a room is Occu for a specific date
        room = form.cleaned_data.get('room')
        date_in = form.cleaned_data.get('date_in')
        date_out = form.cleaned_data.get('date_out')
        status_res = form.cleaned_data.get('status_res')
        reservation_check = Reservation.objects.filter( 
            room = room,
            date_in__lte = date_in,
            date_out__gte = date_out,
            # status_res = status_res,   if not commented gives a wrong result
        )

        if reservation_check:
            messages.error(self.request, 'This room is already reserved')
            return super().form_invalid(form)
        
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)


# Create passanger
class CreatePasanger(generic.CreateView):
    model = Passanger
    template_name = 'reservation.html'
    context_object_name = 'passangers'
    success_url = reverse_lazy('hotel:home')
    fields = [
        'name',
        'dni',
        'tel',
        'country',
        'city',
        'adress',
        'email',
        'birth_date',
        'observations',

    ]
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)



# Login / register.
class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('hotel:login')
    template_name = 'register.html'

    def form_valid(self, form):        
        response = super().form_valid(form)
        messages.success(self.request, '¡Tu cuenta ha sido creada! Por favor inicia sesión.')
        return response
            
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Las contraseñas no coinciden.')        
        return response

