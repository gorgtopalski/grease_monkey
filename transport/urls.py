from django.urls import path
from .views import tranport_control

app_name = 'transport'

urlpatterns = [
    path('control/', tranport_control, name='control'),
]