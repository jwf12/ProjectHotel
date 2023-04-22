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
from .forms import ReservationForm


class Base(generic.ListView):
    model = Room
    template_name = 'base.html'
    context_object_name = 'room'

    def get_queryset(self):
        return super().get_queryset().values_list('type_room', flat=True).distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.get_queryset()
        return context


class Home(generic.ListView):
    queryset = Room.objects.all().order_by('id')
    template_name = 'index.html'
    context_object_name = 'rooms'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(status_res=2) 
        room_change_satate()   
        return context


#Shows passenger info in 'passanger.html'
class ShowPassData(generic.DetailView):
    model = Passanger
    template_name = 'passanger.html'
    context_object_name = 'passan'


#Show rooms in 'index.html'
class ShowRooms(generic.ListView):
    queryset = Room.objects.all().order_by('id')
    template_name = 'rooms.html'
    context_object_name = 'rooms'


#Edit Room
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


#Edit Passenger
class PassangerEditarView(generic.UpdateView):
    model = Passanger
    template_name = 'index.html'
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
        response = super().form_valid(form)
        messages.success(self.request, 'Info edited')
        return response
    
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
        response = super().form_valid(form)
        messages.success(self.request, 'Reservation edited')
        return response
    
    def form_invalid(self,form):
        return super().form_invalid(form)


#modify reservation from Search. 
class UpdateReservationViewSearch(generic.UpdateView):
    model = Reservation    
    success_url = reverse_lazy('hotel:search')
    fields = [
            'room',
            'date_in',
            'date_out',
            'amount_people',
            'observations',
    ]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reservation edited')
        return response
    
    def form_invalid(self,form):
        return super().form_invalid(form)


#Create a reservation.
class CreateReservation(generic.CreateView):
    model = Reservation   
    context_object_name = 'reservations'
    template_name = 'reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('hotel:create_reservation')   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        context['passangers'] = Passanger.objects.all()
        context['today'] = date.today()
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Validating if a room is Occu for a specific date
        room = form.cleaned_data.get('room')
        date_in = form.cleaned_data.get('date_in')
        date_out = form.cleaned_data.get('date_out')
        status_res = form.cleaned_data.get('status_res')
        # reservation_check = Reservation.objects.filter( 
        #     room = room,
        #     date_in__lte = date_in,
        #     date_out__gte = date_out,
        #     status_res = status_res,  
        # )

        # if reservation_check:
        #     messages.error(self.request, 'This room is already reserved')
        #     return super().form_invalid(form)
        
        messages.success(self.request, 'Reservation created')
        return response
    
    def form_invalid(self,form):
        return super().form_invalid(form)


# Create passanger
class CreatePasanger(generic.CreateView):
    model = Passanger
    template_name = 'reservation.html'
    context_object_name = 'passangers'
    success_url = reverse_lazy('hotel:create_reservation')
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
        response = super().form_valid(form)
        messages.success(self.request, 'Passenger created')
        return response
    
    def form_invalid(self, form):
        return super().form_invalid(form)


# Login 
class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)


# register.
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

