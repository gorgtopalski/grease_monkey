from django.urls import path

from working_shift.views import change_shift

app_name = 'working'

urlpatterns = [
    path('shift/', change_shift, name='shift-change'),
]