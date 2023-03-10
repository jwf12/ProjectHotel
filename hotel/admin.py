from django.contrib import admin
from .models import Passanger, Room, Reservation


class PassangerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'dni',
        'tel',
        'email',
        'birth_date',
        'observations',
    )
    list_filter = ('birth_date',)
    search_fields = ('name',)


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'max_capacity',
        'type_room',
        'state',
        'status',
    )
    search_fields = ('name',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'passanger',
        'room',
        'date_in',
        'date_out',
        'number',
        'amount_people',
        'status_res',
        'observations',
    )
    list_filter = ('passanger', 'room', 'date_in', 'date_out')


admin.site.register(Passanger, PassangerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
