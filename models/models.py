from django.db import models

from context.models import Color, Line
from django.urls import reverse

# Create your models here.


class BottleModel(models.Model):
    name = models.CharField('modelo', max_length=200)
    blueprint = models.CharField('plano maqueta', max_length=100, unique=True)

    class Meta:
        ordering = ["blueprint"]

    def __str__(self):
        return f'[{self.blueprint}] {self.name}'

    def get_absolute_url(self):
        return reverse('models:model-show', kwargs={'pk': self.pk})


class Production(models.Model):
    model = models.ForeignKey(BottleModel, on_delete=models.RESTRICT, verbose_name='modelo')
    line = models.ForeignKey(Line, on_delete=models.RESTRICT, verbose_name="línea")
    color = models.ForeignKey(Color, on_delete=models.RESTRICT, verbose_name="color")
    start_date = models.DateField('fecha inicio')
    end_date = models.DateField('fecha final', blank=True, null=True)
    finished = models.BooleanField('finalizada?', default=False)
    speed = models.IntegerField('velocidad', default=0)
    sections = models.IntegerField('secciones', default=0)
    weight = models.IntegerField('peso', default=0)

    def __str__(self):
        return f'{self.line}: {self.model} {self.start_date}-{self.end_date}'

    def get_absolute_url(self):
        return reverse("models:production-show", kwargs={"pk": self.pk})
    

    