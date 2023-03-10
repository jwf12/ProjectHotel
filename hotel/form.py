from .models import Passanger
from django import forms

class PassangerForm(forms.ModelForm):
    
    class Meta:
        model = Passanger
        fields=[
            'name',
            'dni',
            'tel',
            'email',
            'country',
            'city',
            'adress',
            'birth_date',
            'observations',
        ]