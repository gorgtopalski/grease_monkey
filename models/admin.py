from django.contrib import admin

from models.models import BottleModel, Production

# Register your models here.
admin.site.register(BottleModel)
admin.site.register(Production)