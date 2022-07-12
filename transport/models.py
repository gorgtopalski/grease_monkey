from os import nice
from pyexpat import model
from django.db import models

from context.models import Line
from models.models import Production

# Create your models here.

class Transport(models.Model):
    convoyer = models.BooleanField('desfile / convoyer', default=True, blank=True, null=True)
    wheel = models.BooleanField('paso por rueda', default=True, blank=True, null=True)
    cross = models.BooleanField('cross convoyer', default=True, blank=True, null=True)
    lehr = models.BooleanField('puesta en archa', default=True, blank=True, null=True)
    comments = models.TextField('observaciones', blank=True, null=True)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT, verbose_name='línea')
    production = models.ForeignKey(Production, on_delete=models.RESTRICT, verbose_name='producción')
    

class TransportControl(models.Model):
    date = models.DateTimeField('hora control')
    