from hotel.models import Reservation, Room

# Funcion para cambiar el estado del room en caso que se le de check in a la reserva.

def room_change_satate():
    reserved_rooms = set(Reservation.objects.filter(status_res=2).values_list('room__id', flat=True))
    all_rooms = Room.objects.all()
    
    for room in all_rooms:
        if room.id in reserved_rooms:
            room.state = 2
        else:
            room.state = 1
        room.save()
    
    return None
