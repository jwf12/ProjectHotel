from django import template
import django_filters
from .models import Reservation

register = template.Library()

@register.filter
def get_item(value, arg):
    return value.get(arg)




class SearchFilter(django_filters.FilterSet):    
    class Meta:
        model = Reservation
        fields = [
        'passanger',
        'room',
        'date_in',
        'date_out',
        'number',
        'status_res',
        ]