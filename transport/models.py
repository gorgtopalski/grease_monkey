from operator import truediv
from django.db import models
from django.urls import reverse

from models.models import Production
from working_shift.models import WorkingShift

# Create your models here.
class TransportControl(models.Model):
    CHOICE = [
        (True, 'OK'),
        (False, 'KO'),
        (None, ' '),
    ]

    date = models.DateTimeField('hora control')
    working_shift = models.ForeignKey(WorkingShift, on_delete=models.RESTRICT, verbose_name='parte')
    comments = models.TextField('observaciones', blank=True, null=True)
    convoyer_l11a = models.BooleanField('desfile maquina A', default=None, blank=True, null=True, choices=CHOICE)
    convoyer_l11b = models.BooleanField('desfile maquina B', default=None, blank=True, null=True, choices=CHOICE)
    wheel_l11 = models.BooleanField('paso por rueda', default=None, blank=True, null=True, choices=CHOICE)
    cross_l11 = models.BooleanField('cross convoyer', default=None, blank=True, null=True, choices=CHOICE)
    lehr_l11 = models.BooleanField('puesta en archa', default=None, blank=True, null=True, choices=CHOICE)
    production_l11a = models.ForeignKey(Production, on_delete=models.RESTRICT, verbose_name='producción L11A', related_name='prod_l11a')
    production_l11b = models.ForeignKey(Production, on_delete=models.RESTRICT, verbose_name='producción L11B', related_name='prod_l11b')
    convoyer_l14 = models.BooleanField('Desfile', default=None, blank=True, null=True, choices=CHOICE)
    wheel_l14 = models.BooleanField('paso por rueda', default=None, blank=True, null=True, choices=CHOICE)
    cross_l14 = models.BooleanField('cross convoyer', default=None, blank=True, null=True, choices=CHOICE)
    lehr_l14 = models.BooleanField('puesta en archa',default=None, blank=True, null=True, choices=CHOICE)
    production_l14 = models.ForeignKey(Production, on_delete=models.RESTRICT, verbose_name='producción L14', related_name='prod_l14')
    convoyer_l12a = models.BooleanField('desfile maquina A', default=None, blank=True, null=True, choices=CHOICE)
    convoyer_l12b = models.BooleanField('desfile maquina B', default=None, blank=True, null=True, choices=CHOICE)
    wheel_l12 = models.BooleanField('paso por rueda', default=None, blank=True, null=True, choices=CHOICE)
    cross_l12 = models.BooleanField('cross convoyer', default=None, blank=True, null=True, choices=CHOICE)
    lehr_l12 = models.BooleanField('puesta en archa', default=None, blank=True, null=True, choices=CHOICE)
    production_l12 = models.ForeignKey(Production, on_delete=models.RESTRICT, verbose_name='producción L12', related_name='prod_l12')
    convoyer_l13 = models.BooleanField('desfile', default=None, blank=True, null=True, choices=CHOICE)
    wheel_l13 = models.BooleanField('paso por rueda', default=None, blank=True, null=True, choices=CHOICE)
    cross_l13 = models.BooleanField('cross convoyer', default=None, blank=True, null=True, choices=CHOICE)
    lehr_l13 = models.BooleanField('puesta en archa', default=None, blank=True, null=True, choices=CHOICE)
    production_l13 = models.ForeignKey(Production, on_delete=models.RESTRICT, verbose_name='producción L13', related_name='prod_l13')

    def get_absolute_url(self):
        return reverse("transport:control-show", kwargs={"pk": self.pk})