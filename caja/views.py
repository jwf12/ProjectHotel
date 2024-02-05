from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.db.models import Sum
from .models import *
from hotel.models import Reservation

    
class Till_Detail(generic.DetailView):
    model = Till
    template_name = 'till.html'
    context_object_name = 'till'
    
    def get_context_data(self, **kwargs: Any):
            context = super().get_context_data(**kwargs)
            #se crea la variable para los items de determinada reserva
            items = Item_Till.objects.filter(item_till=self.object)
            #se crea la variable para los pagos de determinada reserva
            payments = Payment.objects.filter(payment_till=self.object)

            # Sumar los montos de los items
            total_amount_items = items.aggregate(Sum('price'))['price__sum'] or 0
            # Sumar los montos de las transacciones de pago
            total_amount_pays = payments.aggregate(Sum('amount'))['amount__sum'] or 0
            #la diferencia entre los 2
            total_total =  total_amount_items + total_amount_pays

            # Agregar el total al contexto
            context['total_amount_items'] = total_amount_items
            context['total_amount_pays'] = total_amount_pays
            context['total_total'] = total_total

            # Agregar las transacciones de pago al contexto
            context['items'] = items
            context['payments'] = payments
            
            return context


class Item_Create(generic.CreateView):
    model = Item_Till
    template_name = 'till.html'
    context_object_name = 'items'
    success_url = reverse_lazy('hotel:home')
    fields = [
        'item_till',
        'name',
        'price',
        'observation',  
    ]
      
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Item created')

        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class Payment_Create(generic.CreateView):
    model = Payment
    template_name = 'till.html'
    context_object_name = 'payments'
    success_url = reverse_lazy('hotel:home')
    fields = [
        'payment_till',
        'pay_method',
        'amount',
        'observation',  
    ]
      
    def form_valid(self, form):
        response = super().form_valid(form)
        print(self.request)
        messages.success(self.request, 'Payment created')

        return response
    
    def form_invalid(self, form):
        return super().form_invalid(form)
        
    
class Item_Delete(generic.DeleteView):
     model = Item_Till
     success_url = reverse_lazy('hotel:home')


class Payment_Delete(generic.DeleteView):
     model = Payment
     success_url = reverse_lazy('hotel:home')