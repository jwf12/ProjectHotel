from hotel.models import Reservation, Room

# Funcion para cambiar el estado del room en caso que se le de check in a la reserva.

def room_change_satate():
    reserved_rooms = Reservation.objects.filter(status_res=2).values_list('room__id', flat=True)
    free_rooms = Room.objects.exclude(id__in=reserved_rooms)
    free_rooms.update(state=1)
    return None

# Funcion para cambiar el estado del room cuando los pax salen de la habitacion. 
# def room_change_state_passanger():
#     context = Room.objects.filter(passanger=)

