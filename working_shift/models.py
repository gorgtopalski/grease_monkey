from django.db import models
from django.contrib.auth.models import User
from context.models import Team, Shift


class WorkingShift(models.Model):
    specialist_vc1 = models.ForeignKey(User, verbose_name='especialista vc 1', blank=True, null=True, on_delete=models.RESTRICT, related_name='esp_vc_1')
    specialist_vc2 = models.ForeignKey(User, verbose_name='especialista vc 2', blank=True, null=True, on_delete=models.RESTRICT, related_name='esp_vc_2')
    team = models.ForeignKey(Team, verbose_name='equipo', on_delete=models.RESTRICT)
    shift = models.ForeignKey(Shift, verbose_name='turno', on_delete=models.RESTRICT)
    date = models.DateField('fecha')