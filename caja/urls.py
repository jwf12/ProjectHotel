from django.urls import path
from .views import  Till_Detail, Item_Create, Payment_Create, Item_Delete, Payment_Delete

app_name='caja'

urlpatterns = [ 
        path('till/<int:pk>/', Till_Detail.as_view(), name='till'),
        path('create-item/', Item_Create.as_view(), name='item_create'),
        path('create-payment/', Payment_Create.as_view(), name='payment_create'),
        path('delete-item/<int:pk>/', Item_Delete.as_view(), name='delete-item'),
        path('delete-payment/<int:pk>/', Payment_Delete.as_view(), name='delete-payment'),


]
