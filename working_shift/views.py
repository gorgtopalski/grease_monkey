from datetime import datetime
from django.shortcuts import render, redirect
from context.models import Shift, Team
from working_shift.forms import ShiftChangeForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def change_shift(request):

    def get_shift():
        now = datetime.now()
        if now.hour >= 6 and now.hour < 14:
            return Shift.objects.get(shift_name='Mañana').id
        elif now.hour >= 14 and now.hour < 22:
            return Shift.objects.get(shift_name='Tarde').id
        else:
            return Shift.objects.get(shift_name='Noche').id

    def get_team():

        SHIFTS = [
         #1  M,T,N
            [1,3,5],
            [1,3,5],
            [4,1,3],
            [4,1,3],
            [5,4,1],
            [5,4,1],
            [5,4,1],
         #2  M,T,N
            [3,2,4],
            [3,2,4],
            [1,3,2],
            [1,3,2],
            [4,1,3],
            [4,1,3],
            [4,1,3],
         #3  M,T,N
            [2,5,1],
            [2,5,1],
            [3,2,5],
            [3,2,5],
            [1,3,2],
            [1,3,2],
            [1,3,2],
        #3  M,T,N
            [5,4,3],
            [5,4,3],
            [2,5,4],
            [2,5,4],
            [3,2,5],
            [3,2,5],
            [3,2,5],
        #4  M,T,N
            [4,1,2],
            [4,1,2],
            [5,4,1],
            [5,4,1],
            [2,5,4],
            [2,5,4],
            [2,5,4],
        ]

        # based of the circular calendar
        INITIAL_DATE = '03/01/2022'
        delta = (datetime.now() - datetime.strptime(INITIAL_DATE, "%d/%m/%Y")).days
        array_position = get_shift()-1

        delta = (delta % len(SHIFTS))
        val = SHIFTS[delta]

        try:
            team = Team.objects.get(team=val[array_position])
        except ObjectDoesNotExist:
            team = None

        return team

    if request.method == 'POST':
        form = ShiftChangeForm(request.POST)
        if form.is_valid():
            ws = form.save()
            request.session.flush()
            request.session['working_shift_id'] = ws.id
            
            return redirect('dashboard:home')
    else:
        form = ShiftChangeForm()
        form.initial = {
            "shift": get_shift(),
            "team": get_team(),
        }

    return render(request, 'working_shift/change_shift_form.html', {'form': form })