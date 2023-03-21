from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from hotel.models import Passanger, Reservation
from weasyprint import HTML
from datetime import datetime
from django.template.loader import get_template 
from weasyprint.text.fonts import FontConfiguration
from django.shortcuts import get_object_or_404

def export_pdf(request, pk):
    passanger = get_object_or_404(Reservation, pk=pk)
    context = {
        # Pass info
        'name': passanger.passanger.name,
        'Id': passanger.passanger.dni,
        'age': passanger.passanger.birth_date,
        'tel': passanger.passanger.tel,
        'email': passanger.passanger.email,

        # Rva info
        'num_rva': passanger.number,
        'in': passanger.date_in,
        'out': passanger.date_out,
        'people': passanger.amount_people,
        'obs': passanger.observations,
        'room': passanger.room.name,
        'room_type': passanger.room.type_room,

        # Otros
        'current_date': datetime.now(),
    }
    html_template = get_template('printinfo.html')
    html_string = html_template.render({'person': passanger})
    html_string = html_template.render(context)
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{passanger.passanger.name}.pdf"'
    return response
