from django.db import models
from django.contrib.auth.models import User
from AppBcs.models import *

# Create your models here.
class Avatar(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    imagen=models.ImageField(upload_to='Avatares',null=True,blank=True)

    def __str__(self):
        return f"Imagen de {self.user.username}"


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE, null=True, blank=True)
    periferico = models.ForeignKey(Periferico, on_delete=models.CASCADE, null=True, blank=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, null=True, blank=True)
    funko = models.ForeignKey(Funko, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        producto = self.consola or self.periferico or self.juego or self.funko
        return f"{self.cantidad} x {producto.nombre} en el carrito de {self.carrito.usuario.username}"

    @property
    def precio(self):
        producto = self.consola or self.periferico or self.juego or self.funko
        return producto.precio * self.cantidad
 