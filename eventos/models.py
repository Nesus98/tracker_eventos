from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Candidatura(models.Model):
    ESTADOS = (
        ('ENVIADA', 'Curriculum Enviado'),
        ('ENTREVISTA', 'En proceso de entrevista'),
        ('ACEPTADA', '¡Contratado!'),
        ('RECHAZADA', 'Descartado'),
    )

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='candidaturas')
    puesto = models.CharField(max_length=150)
    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default='ENVIADA'
    )
    fecha_aplicacion = models.DateField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.puesto} - {self.evento.nombre} ({self.estado})"