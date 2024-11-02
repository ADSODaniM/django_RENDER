from django.db import models

# Create your models here.
class Servicio(models.Model):    
    TIPO_CHOICES = [
        ('manicura', 'Manicura'),
        ('pedicura', 'Pedicura'),
        ('otros', 'Otros'),  # Otras opciones que puedas necesitar
    ]
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_servicio = models.CharField(max_length=20, choices=TIPO_CHOICES, null=True, blank=True)
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __str__(self):
        return self.nombre_servicio
