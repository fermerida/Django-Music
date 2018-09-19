from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Album(models.Model):
    id_album = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class AlbumCancion(models.Model):
    id_album_cancion = models.FloatField(primary_key=True)
    album = models.CharField(max_length=50, blank=True, null=True)
    cancion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album_cancion'


class Artista(models.Model):
    id_artista = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artista'

class Cancion(models.Model):
    id_cancion = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha_lanzamiento = models.CharField(max_length=50, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancion'


class CancionLista(models.Model):
    id_cancion_lista = models.FloatField(primary_key=True)
    cancion = models.CharField(max_length=50, blank=True, null=True)
    lista = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancion_lista'


class Conteo(models.Model):
    id_conteo = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'conteo'

class Genero(models.Model):
    id_genero = models.FloatField(primary_key=True)
    genero = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'


class Lista(models.Model):
    id_lista = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista'


class Usuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    usuario = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    foto = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.FloatField(blank=True, null=True)
    clave = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('correo', 'usuario'),)


class UsuarioArtista(models.Model):
    id_usuario_artista = models.FloatField(primary_key=True)
    usuario = models.CharField(max_length=50)
    artista = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_artista'


class UsuarioLista(models.Model):
    id_usuario_lista = models.FloatField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    lista = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_lista'





















