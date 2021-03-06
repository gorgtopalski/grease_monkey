from django.db import models

# Create your models here.

class Line(models.Model):
    line = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.line}'


class Team(models.Model):
    team = models.IntegerField()

    def __str__(self):
        return f'{self.team}'


class Shift(models.Model):
    shift = models.IntegerField()
    shift_name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.shift_name}'


class Color(models.Model):
    color = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.color}'