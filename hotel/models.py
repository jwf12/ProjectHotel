from django.db import models
from django.contrib.auth.models import User

class Passanger(models.Model):
    name = models.CharField(max_length=205)
    dni = models.CharField(max_length=205)
    tel = models.CharField(max_length=205)
    email = models.EmailField()
    birth_date = models.DateField()
    observations = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    STATE_STATE=(  
        (1, 'free'),
        (2, 'occupied'),
        )   
    STATUS_COLOR=(
        (1, 'success'), # clean
        (2, 'warning'), # dirty
        (3, 'danger',)  # blocked
    )

    max_capacity = models.CharField(max_length=205)
    name = models.CharField(max_length=205)
    type_room = models.CharField(max_length=205)
    state = models.IntegerField(choices=STATE_STATE, default=1)
    status = models.IntegerField(choices=STATUS_COLOR, default=1)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    STATUS_RESERVATION=(  
            (1, 'reserved'),
            (2, 'check-in'),
            (3, 'check-out'),
        )
    
    passanger = models.ForeignKey(Passanger, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_in = models.DateField()
    date_out = models.DateField()
    number = models.CharField(max_length=20)
    amount_people = models.IntegerField()
    status = status = models.IntegerField(choices=STATUS_RESERVATION)
    observations = models.TextField()



