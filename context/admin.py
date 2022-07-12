from django.contrib import admin

from context.models import Color, Line, Shift, Team

# Register your models here.
admin.site.register(Shift)
admin.site.register(Team)
admin.site.register(Line)
admin.site.register(Color)