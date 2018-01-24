from django.contrib import admin
from .models import Consulta, Opcion, Invitacion, Votacion
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Opcion
    extra = 2

class votarOpcion(admin.ModelAdmin):
    list_display = ('titulo','consulta','autor','fechaInicio','fechaFinal')
    inlines = [ChoiceInline]

class adminOpcion(admin.ModelAdmin):
	list_display = ('consulta','opcion','votos')
	list_filter = ['consulta','opcion','votos']

class adminVotar(admin.ModelAdmin):
	list_display = ('consulta','opcion','autor')

admin.site.register(Consulta, votarOpcion)
admin.site.register(Opcion,adminOpcion)
admin.site.register(Invitacion)
admin.site.register(Votacion,adminVotar)