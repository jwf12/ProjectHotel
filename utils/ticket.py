from django.http import HttpResponse
from django.template.loader import get_template 
from django.shortcuts import get_object_or_404
from xhtml2pdf import pisa
from io import BytesIO
from datetime import datetime
from hotel.models import Passanger, Reservation

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
        'room': passanger.room.name if passanger.room else '',
        'room_type': passanger.get_type_res_display,

        # Otros
        'current_date': datetime.now(),
    }
    html_template = get_template('ProjectHotel/templates/printInfo.html')
    html_string = html_template.render({'person': passanger})
    html_string = html_template.render(context)

    pdf_file = BytesIO()
    pisa.CreatePDF(html_string, dest=pdf_file)
    pdf_file.seek(0)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{passanger.passanger.name} Reservation.pdf"'
    return response

