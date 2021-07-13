from django.db import models

#Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="Id de Categoria")
    Categoria = models.CharField(max_length=50,verbose_name="Nombre de la categoria")
    
    def __str__(self):
        return self.Categoria


class Periodista(models.Model):
    NombrePeriodista = models.CharField( max_length=50 ,verbose_name="nombre de periodista")
    Edad =models.IntegerField(verbose_name="edad")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Ocupacion = models.CharField( max_length=200 ,verbose_name="ocupacion")
    CantidadNoticias = models.IntegerField(verbose_name="cantidad de noticias")
    imagen = models.ImageField(upload_to="periodistas",null=True)
    def __str__(self):
        return self.NombrePeriodista

class Noticia(models.Model):
    NombreNoticia = models.CharField( max_length=500 ,verbose_name="nombre de la noticia")
    Fecha =models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Ubicacion = models.CharField( max_length=200 ,verbose_name="ubicacion")
    autor =models.ForeignKey(Periodista, on_delete=models.CASCADE, max_length=50,verbose_name="periodista")
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="noticias",null=True)
    def __str__(self):
        return self.NombreNoticia

opciones_consultas=[
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencias"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre=models.CharField( max_length=50)
    correo =models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre