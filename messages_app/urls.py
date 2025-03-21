from django.urls import path
from .views import inbox, send_message

app_name = 'messages'
urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('send/', send_message, name='send_message'),
]