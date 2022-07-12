from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserCreateForm


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = first_name[:1]+str(hash(last_name + first_name))[:10]

            user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
            user.set_unusable_password()
            user = user.save()

            return redirect('dashboard:home')

    else:
        form = UserCreateForm()

    return render(request, 'users/create_user.html', {'form':form} )
    

    


