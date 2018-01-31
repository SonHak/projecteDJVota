from django.contrib import admin
from .models import Consulta, Opcion, Invitacion, Votacion
# Register your models here.


class ChoiceInline(admin.TabularInline):
	model = Opcion
	extra = 2


class crearConsula(admin.ModelAdmin):
	list_display = ('titulo','consulta','autor','fechaInicio','fechaFinal')
	inlines = [ChoiceInline]
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(autor=request.user)


class adminOpcion(admin.ModelAdmin):
	list_display = ('consulta','opcion','votos')
	list_filter = ['consulta','opcion','votos']
	
class adminVotar(admin.ModelAdmin):
	list_display = ('consulta','opcion','autor')
	

class adminInvitar(admin.ModelAdmin):
	list_display=('consulta','email')


admin.site.register(Consulta, crearConsula)
admin.site.register(Opcion,adminOpcion)
admin.site.register(Invitacion,adminInvitar)
admin.site.register(Votacion,adminVotar)