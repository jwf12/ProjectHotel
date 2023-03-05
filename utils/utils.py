from hotel.models import Reservation, Room
# Funcion para cambiar el estado del room en caso que se le de check in a la reserva.
def room_change_satate():
    context = Reservation.objects.filter(status_res=2)
    if context:
        for con in context:
            pk_res = con.room.id
            room_get = Room.objects.get(id=pk_res)
            room_get.state = 2
            room_get.save()
    return None


# Funcion para cambiar el estado del room cuando los pax salen de la habitacion. 
# def room_change_state_passanger():
#     context = Room.objects.filter(passanger=)

