from django.urls import path

from dashboard.views import DashboardView, shift_change

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('shift/', shift_change, name='shift-change'),
]