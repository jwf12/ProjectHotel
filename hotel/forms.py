from .models import Reservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
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
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ReservationForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['room'].required = False