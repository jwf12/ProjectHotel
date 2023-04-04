from django.db import models
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField

class Passanger(models.Model):
    name = models.CharField(max_length=205)
    dni = models.CharField(max_length=205)
    tel = models.CharField(max_length=205)
    country = models.CharField(max_length=205, null=True, blank=True)
    city  = models.CharField(max_length=205, null=True, blank=True)
    adress  = models.CharField(max_length=205, null=True, blank=True)
    email = models.CharField(max_length=205, null=True, blank=True)
    birth_date = models.DateField()
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    STATE_STATE=(  
        (1, 'free'),
        (2, 'occupied'),
        )   
    STATUS_COLOR=(
        ('#9bf0ac', 'clean'), # clean 
        ('#fffb8f', 'dirty'), # dirty 
        ('#D47777', 'blocked'),  # blocked 
    )
    TYPES_ROOMS=(
        ('1', 'Sgl'),
        ('2', 'Dbl'),
        ('3', 'Tpl'),
        ('4', 'Qdpl'),
    )
    
    max_capacity = models.CharField(max_length=205)
    name = models.CharField(max_length=205)
    type_room = models.CharField(max_length=4, choices=TYPES_ROOMS, default='1') 
    state = models.IntegerField(choices=STATE_STATE, default=1)
    status = models.CharField(max_length=7, choices=STATUS_COLOR, default='#9bf0ac')
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    STATUS_RESERVATION=(
            (1, 'reserved'),
            (2, 'check-in'),
            (3, 'check-out'),
            (4, 'no-show'),
        )
    TYPES_ROOMS=(
        ('1', 'Sgl'),
        ('2', 'Dbl'),
        ('3', 'Tpl'),
        ('4', 'Qdpl'),
    )
    
    passanger = models.ForeignKey(Passanger, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True,null=True, default=None)
    type_res = models.CharField(max_length=4, choices=TYPES_ROOMS, default='1')
    date_in = models.DateField()
    date_out = models.DateField()
    number = ShortUUIDField(length=6)
    amount_people = models.IntegerField()
    status_res = models.IntegerField(choices=STATUS_RESERVATION, default = 'not-reserved')
    observations = models.TextField()

