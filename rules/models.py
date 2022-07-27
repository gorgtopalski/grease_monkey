from django.db import models
from django.urls import reverse
from models.models import Production

# Create your models here.

class Rules(models.Model):
    production = models.ForeignKey(Production, on_delete=models.RESTRICT)
    
    gob = models.IntegerField('longitud gota', blank=True, null=True)
    gob_max = models.IntegerField('+', blank=True, null=True, default=20)
    gob_min = models.IntegerField('-', blank=True, null=True, default=20)

    feeder = models.IntegerField('Tª derrame', blank=True, null=True)
    feeder_max = models.IntegerField('+', blank=True, null=True, default=5)
    feeder_min = models.IntegerField('-', blank=True, null=True, default=5)

    blank_side = models.IntegerField('Tª preparador', blank=True, null=True)
    blank_side_max = models.IntegerField('+', blank=True, null=True, default=20)
    blank_side_min = models.IntegerField('-', blank=True, null=True, default=20)

    finish_side = models.IntegerField('Tª terminador', blank=True, null=True)
    finish_side_max = models.IntegerField('+', blank=True, null=True, default=20)
    finish_side_min = models.IntegerField('-', blank=True, null=True, default=20)

    def get_absolute_url(self):
        return reverse('rules:rules-show', kwargs={'production': self.production.id })