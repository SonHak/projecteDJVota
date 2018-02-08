from django.conf import settings
from django.db import models

# Create your models here.
class Consulta(models.Model):
	titulo = models.CharField(max_length=200)
	consulta = models.TextField(max_length=300)
	autor = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)
	fechaInicio = models.DateTimeField('Fecha de Inicio')
	fechaFinal = models.DateTimeField('Fecha Final')

	
	
	def __str__(self):
		return self.titulo

	def opciones(self):
		qs = Opcion.objects.filter(consulta = self)
		return list(qs)

class Opcion(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
	opcion = models.CharField(max_length=200)
	votaciones = models.IntegerField(default=0)
	
	def votar(self):
		qs = Opcion.objects.filter(votacion__opcion = self.id)
		return len(qs)

	def __str__(self):
		return self.opcion

class Votacion(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
	opcion = models.ForeignKey(Opcion,on_delete=models.CASCADE)
	autor = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)


	
class Invitacion(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
	email = models.CharField(max_length=200)
