from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Empresa',unique=True)
    contacto=models.CharField(max_length=50, blank=True, null=True)
    correo =  models.EmailField(max_length=100, blank=True, null=True)


    def __str__(self):
        return "{}".format(self.nombre)
    class Meta:
        verbose_name = 'Empresa'
        ordering = ('nombre',)

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100,unique=True, blank=True, null=True)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categoria"
        ordering = ['descripcion','id']
    def __str__(self):
        return "{} - {}".format(self.descripcion,self.id)

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False,null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name="Productos"
        verbose_name_plural="Productos"
        ordering = ['nombre']
    def __str__(self):
        return "{} - {} - {}".format(self.categoria.descripcion,self.id,self.nombre)



class Postulante(models.Model):
    nombres = models.CharField(max_length=200, unique=True)
    apellidos = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=100, unique=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    archivo = models.FileField(upload_to='usuar/media', blank=True, null=True)


    def __str__(self):
        return "{}".format(self.nombres)

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulante"
        ordering = ('nombres',)

    def get_archivo(self):
        if self.archivo:
            return '{}{}'.format(settings.MEDIA_URL, self.archivo)
        return '{}{}'.format(settings.STATIC_URL, 'usuar/media')

