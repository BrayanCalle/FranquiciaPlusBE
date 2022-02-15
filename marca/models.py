from random import choice
from django.db import models
import os

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    iconofp = models.CharField(max_length=10, verbose_name="Icono de la Categoría", null = True)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=30, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=30, unique=True, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre

class Directorio(models.Model):
    nombre = models.CharField(max_length=30, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Inversion(models.Model):
    nombre = models.CharField(max_length=30, unique=True, verbose_name="Rango de Inversión")

    def __str__(self):
        return self.nombre

# class Estrellas(models.Model):
#     nombre = models.IntegerField(unique=True, verbose_name="Número de Estrellas")

#     def __str__(self):
#         return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=20, unique=True, verbose_name="Nombre de la Prioridad")
    valor = models.IntegerField(unique=True, null=True, verbose_name="Prioridad en orden de franquicias")

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=30, unique=True, verbose_name="Nombre")
    precio = models.IntegerField(verbose_name="Precio", default=0)
    inversion = models.ForeignKey(Inversion, on_delete=models.CASCADE, verbose_name="Rango de Inversión")
    descripcion = models.TextField(max_length=150 ,verbose_name="Descripción")
    imagenmarca = models.ImageField(upload_to='photos/franquicia/marca', verbose_name="Imagen Marca")
    imagenlocal = models.ImageField(upload_to='photos/franquicia/local', verbose_name="Imagen Local")
    imagenlogo = models.ImageField(upload_to='photos/franquicia/logo', verbose_name="Imagen Logo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="marcas")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="marcas", null=True, blank=True, help_text="Recuerde que solo puede agregar 9 marcas en Promoción y solo 6 marcas en Nuevo")
    ubicacion = models.ManyToManyField(Ubicacion, related_name="marcas")
    directorio = models.ManyToManyField(Directorio, related_name="marcas", blank=True)
    # estrellas = models.ForeignKey(Estrellas, on_delete=models.CASCADE, verbose_name="Número de estrellas", null=True, blank=True)
    numeroestrellas = (
        ('1','Una'),
        ('2','Dos'),
        ('3','Tres'),
        ('4','Cuatro'),
        ('5','Cinco'),
    )
    estrellas = models.CharField(choices=numeroestrellas, max_length=5, help_text="Número de estrellas que se le asigna a la marca")
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, verbose_name="Prioridad en el orden de franquicias", blank=True, null=True)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Marca.objects.get(id=self.id)
        except Marca.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.imagenmarca and self.imagenmarca and obj.imagenmarca != self.imagenmarca:
            # delete the old image file from the storage in favor of the new file
            obj.imagenmarca.delete()
        elif obj.imagenlocal and self.imagenlocal and obj.imagenlocal != self.imagenlocal:
            obj.imagenlocal.delete()
        elif obj.imagenlogo and self.imagenlogo and obj.imagenlogo != self.imagenlogo:
            obj.imagenlogo.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.imagenmarca.delete()
        self.imagenlocal.delete()
        self.imagenlogo.delete()
        return super(Marca, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Marca, self).save(*args, **kwargs)

    def __str__(self):
        return "{} Precio: {}".format(self.nombre, self.precio)