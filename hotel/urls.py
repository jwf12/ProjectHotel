from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, CustomLoginView, SingUpView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),
]
