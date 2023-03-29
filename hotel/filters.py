from django import template
import django_filters
register = template.Library()

@register.filter
def get_item(value, arg):
    return value.get(arg)

from .models import Reservation
import django_filters


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