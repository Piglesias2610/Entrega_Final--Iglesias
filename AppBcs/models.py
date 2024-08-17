from django.db import models

# Clase Consola
class Consola(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='consolas/', null=True, blank=True)  # Campo para la imagen

    def __str__(self):
        return f"Consola: {self.nombre} - Precio: {self.precio} soles"

# Clase Periferico
class Periferico(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)  # Ejemplo: "Teclado", "Ratón", "Control"
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='perifericos/', null=True, blank=True)  # Campo para la imagen

    def __str__(self):
        return f"Periférico: {self.nombre} ({self.tipo}) - Marca: {self.marca} - Precio: {self.precio} soles"

# Clase Juegos
class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)  # Ejemplo: "Acción", "Aventura", "Deportes"
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)  # Relación con Consola
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)  # Campo para la imagen

    def __str__(self):
        return f"Juego: {self.nombre} - Género: {self.genero} - Consola: {self.consola.nombre} - Precio: {self.precio} soles"

# Clase Funkos
class Funko(models.Model):
    nombre = models.CharField(max_length=50)
    personaje = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)  # Ejemplo: "Marvel", "Star Wars"
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='funkos/', null=True, blank=True)  # Campo para la imagen

    def __str__(self):
        return f"Funko: {self.nombre} - Personaje: {self.personaje} - Serie: {self.serie} - Precio: {self.precio} soles"
