from django.urls import path

from users.views import create_user

app_name = 'users'

urlpatterns = [
    path('add/', create_user, name='user-add'),
]