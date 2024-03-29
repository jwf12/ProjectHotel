from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, CustomLoginView, SingUpView,  PassangerEditarView, ShowPassData, UpdateReservationView, ShowRooms, RoomEditarView, CreateReservation, CreatePasanger,UpdateReservationViewSearch, Base
from utils.ticket import export_pdf
from utils.utils import room_checkout, room_clean, room_blocked, room_dirty, searchView, check_in, no_show



urlpatterns = [
    path('', Home.as_view(), name='home'),

    # user
    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),

    # passanger info passanger.html
    path('pass-info/<int:pk>', ShowPassData.as_view(), name = 'passanger-data'),
    path('update/<int:pk>', PassangerEditarView.as_view(), name='update'),

    #reservations edit in index.html
    path('reservations/update/<int:pk>', UpdateReservationView.as_view(), name='update_reserva'),
    #create reservation
    path('create-reservation/', CreateReservation.as_view(), name = 'create_reservation'),
    #create passanger in reservation.html modal
    path('create-passenger/', CreatePasanger.as_view(), name='create-passenger'),
    
    #Rooms
    path('rooms/', ShowRooms.as_view(), name='room'),
    path('room/<int:pk>', RoomEditarView.as_view(), name='update_room'),
    #status buttons in room.html
    path('room/clean/<int:pk>', room_clean, name='room_clean'),
    path('room/blocked/<int:pk>', room_blocked, name='room_blocked'),
    path('room/dirty/<int:pk>', room_dirty, name='room_dirty'),

    #utils
    path('pdf/<int:pk>/', export_pdf, name='export_pdf'),
    path('checkout/<int:pk>', room_checkout, name='checkout'),
    #search 
    path('search/', searchView, name='search'),
    path('search/check_in/<int:pk>', check_in, name='checkin'),
    path('search/no_show/<int:pk>', no_show, name='noshow'),
    path('search_update/<int:pk>', UpdateReservationViewSearch.as_view(), name='search_update'),

    path('base/', Base.as_view(), name='base')
    ]
