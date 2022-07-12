from django.shortcuts import render, redirect
from working_shift.forms import ShiftChangeForm

# Create your views here.

def change_shift(request):
    if request.method == 'POST':
        form = ShiftChangeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            ws = form.save()
            request.session.flush()
            request.session['working_shift_id'] = ws.id
            
            return redirect('dashboard:home')
    else:
        form = ShiftChangeForm()

    return render(request, 'working_shift/change_shift_form.html', {'form': form })