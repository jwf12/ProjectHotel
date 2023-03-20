from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Passanger, Room, Reservation
from utils.utils import room_change_satate
from django.shortcuts import get_object_or_404
from datetime import date
from django.utils import timezone
from datetime import timedelta


#  Random id reservation: numbershortuuid.ShortUUID().random(length=6) 

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


#modificar reserva. 
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










# class RoomCalendarView(generic.TemplateView):
#     template_name = 'calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         # Obtener la fecha actual y el primer día del mes actual
#         now = timezone.now()
#         month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

#         # Calcular los días del mes actual
#         days = []
#         for i in range(31):
#             day = month_start + timedelta(days=i)
#             if day.month != now.month:
#                 break
#             days.append({
#                 'day': day.day,
#                 'weekday': day.strftime('%a'),
#                 'date': day,
#             })

#         # Calcular la lista de años y meses
#         years = range(now.year, now.year + 5)
#         months = []
#         for i in range(1, 13):
#             month = month_start.replace(month=i)
#             months.append({
#                 'month': i,
#                 'name': month.strftime('%B'),
#             })

#         # Obtener todas las habitaciones y las reservas para el mes actual
#         rooms = Room.objects.all()
#         reservations = Reservation.objects.filter(
#             date_out__gte=month_start,
#             date_in__lte=now.replace(day=31),
#         ).select_related('room')

#         # Calcular las reservas por habitación y día
#         room_reservations = {}
#         for room in rooms:
#             room_reservations[str(room.pk)] = {}
#             for day in days:
#                 room_reservations[str(room.pk)][day['date'].strftime('%Y-%m-%d')] = 0

#         for reservation in reservations:
#             for day in days:
#                 if reservation.date_in <= day['date'] and reservation.date_out > day['date']:
#                     room_reservations[str(reservation.room.pk)][day['date'].strftime('%Y-%m-%d')] += reservation.amount_people

#         context['room_reservations'] = room_reservations
#         context['years'] = years
#         context['months'] = months
#         context['current_year'] = now.year
#         context['days'] = days
#         context['rooms'] = rooms
#         context['room_reservations'] = room_reservations
#         context['Room'] = Room
#         return context