from django.contrib import admin
from .models import Consulta, Opcion, Invitacion, Votacion
# Register your models here.


class ChoiceInline(admin.TabularInline):
	model = Opcion
	extra = 2


class adminConsulta(admin.ModelAdmin):
	readonly_fields = ['autor']
	list_display = ('titulo','consulta','autor','opciones','fechaInicio','fechaFinal')
	list_filter = ['consulta','autor','fechaInicio','fechaInicio','fechaFinal']
	inlines = [ChoiceInline]



	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(autor=request.user)


	def save_model(self, request, obj, form, change):
		obj.autor = request.user
		super(adminConsulta,self).save_model(request, obj, form, change)



class adminOpcion(admin.ModelAdmin):
	readonly_fields = ['consulta']
	list_display = ('opcion','votar','consulta')
	list_filter = ['consulta','opcion']


	
class adminVotar(admin.ModelAdmin):
	list_display = ('opcion','autor')
	

class adminInvitar(admin.ModelAdmin):
	list_display=('consulta','email')


admin.site.register(Consulta,adminConsulta)
admin.site.register(Opcion,adminOpcion)
admin.site.register(Invitacion,adminInvitar)
admin.site.register(Votacion,adminVotar)