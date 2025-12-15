from django.db import models

# Create your models here.
class Pedido(models.Model):
    ESTADOS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.CharField(max_length=100)   # CharField almacena texto corto con un máximo de caracteres.
    fecha_pedido = models.DateField(null=True, blank=True)  # null=True → se permite guardar NULL en la BD blank=True → se permite dejar el campo vacío en formularios
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='pendiente')   # Estado actual del pedido, limitado a las opciones ESTADOS_CHOICES.
    # default='pendiente' → si no se especifica, asumirá "pendiente".

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.producto} ({self.id})"