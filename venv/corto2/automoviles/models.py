from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Marca(models.Model):
	"""docstring for Carros"""
	nombre = models.CharField(max_length = 100)
	pais = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre

class Auto(models.Model):
	"""docstring for Auto"""
	tipo = 	models.CharField(max_length = 100)
	year = models.IntegerField(default = 0)
	marca = models.ForeignKey(Marca, on_delete = models.CASCADE)

	def __str__(self):
		return self.marca, self.tipo, self.year

