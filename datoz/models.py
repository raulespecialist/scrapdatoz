from django.conf import settings
from django.db import models
from django.utils import timezone

# Modelo de los productos.
class Producto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    sku = models.CharField(max_length=200, blank=True, null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    price = models.FloatField(null=False, blank=False)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre