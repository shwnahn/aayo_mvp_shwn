from django.urls import path
from .views import *

app_name = 'aayo'  # URL 네임스페이스 추가

urlpatterns = [
    path('', index, name='index'),
    path('create-room/', create_room, name='create_room'),
    path('room/<str:unique_link>/', room, name='room'),
    path('room/<str:unique_link>/login/', login_room, name='login_room'),
    path('room/<str:unique_link>/order/', order, name='order'),
]