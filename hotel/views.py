from django.shortcuts import render
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
from .form import PassangerForm

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
    model = Reservation
    template_name = 'passanger.html'
    context_object_name = 'passan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allpassan'] = Passanger.objects.get()
        return context



class PassangerEditarView(generic.UpdateView):
    model = Passanger
    template_name = 'passanger.html'
    fields = ['name', 'dni', 'tel', 'email', 'country', 'city', 'adress', 'birth_date', 'observations']
    context_object_name = 'passan'
    success_url = reverse_lazy('hotel:home')

    def get_object(self):
        return get_object_or_404(Passanger, id=self.kwargs['pk'])
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)


# Login / register.
class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)


#modificar reserva. 
class UpdateReservationView(generic.UpdateView):
    model = Reservation
    success_url = reverse_lazy('hotel:home')
    fields = [
        'room',
        'date_in',
        'date_out',
        'number',
        'amount_people',
        'observations'
    ]

    def form_valid(self, form ):
        return super().form_valid(form)


    def form_invalid(self, form ):
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