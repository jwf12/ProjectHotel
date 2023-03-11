from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, CustomLoginView, SingUpView, ShowPassData, PassangerEditarView, UpdateReservationView
from utils.ticket import export_pdf
from utils.utils import room_checkout



urlpatterns = [
    path('', Home.as_view(), name='home'),

    # user
    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),

    # passanger info
    path('pass-info/<int:pk>', ShowPassData.as_view(), name = 'passanger-data'),
    path('update/<int:pk>', PassangerEditarView.as_view(), name='update'),

    #reservations 
    path('reservations/update/<int:pk>', UpdateReservationView.as_view(), name='update_reserva'),

    #utils
    path('pdf/<int:pk>/', export_pdf, name='export_pdf'),
    path('checkout/<int:pk>', room_checkout, name='checkout'),
]
