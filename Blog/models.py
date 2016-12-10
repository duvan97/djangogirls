from django.db import models

# Create your models here.
class Art(models.Model):
	titulo = models.CharField(max_length = 30)
	descripcion = models.TextField()
	fecha = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.titulo