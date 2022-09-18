from django.urls import path

from .views import TransportControlCreateView, TransportControlListView, TransportControlUpdateView, tranport_control

app_name = 'transport'

urlpatterns = [
    path('go/', tranport_control, name='control'),
    path('control/', TransportControlCreateView.as_view(), name='control-create'),
    path('control/<int:pk>/update', TransportControlUpdateView.as_view(), name='control-update'),
    path('control/list', TransportControlListView.as_view(), name='control-list'),
]