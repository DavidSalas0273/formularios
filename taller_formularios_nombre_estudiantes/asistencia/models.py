from django.db import models


class Asistencia(models.Model):
	nombre_completo = models.CharField('Nombre completo', max_length=150)
	documento_identidad = models.CharField('Documento de identidad', max_length=50)
	correo_electronico = models.EmailField('Correo electrónico')
	fecha_asistencia = models.DateField('Fecha de asistencia')
	hora_ingreso = models.TimeField('Hora de ingreso')
	hora_salida = models.TimeField('Hora de salida')
	presente = models.BooleanField('Presente', default=True)
	observaciones = models.TextField('Observaciones', blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.nombre_completo} - {self.fecha_asistencia}"
