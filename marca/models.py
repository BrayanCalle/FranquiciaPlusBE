from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre

class Directorio(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    precio = models.IntegerField(verbose_name="Precio", default=0)
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="marcas")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="marcas", null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name="marcas")
    directorio = models.ForeignKey(Directorio, on_delete=models.CASCADE, related_name="marcas", null=True, blank=True)

    def __str__(self):
        return "{} Precio: {}".format(self.nombre, self.precio)