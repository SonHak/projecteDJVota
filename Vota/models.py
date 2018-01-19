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

class Opcion(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
	opcion = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

class Invitacion(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
