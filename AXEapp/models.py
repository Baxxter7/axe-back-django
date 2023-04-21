from django.db import models
from django.utils import timezone

#Seguridad Roles modelos 1
class Seg_Roles(models.Model):
    cod_rol = models.AutoField(primary_key=True, default=-1)
    tip_roles = models.CharField(max_length=20,default=-1)
    
    class Meta:
        db_table = 'seg_roles'

#Seguridad Permisos modelos 2
class Seg_Permisos(models.Model):
    cod_permisos = models.AutoField(primary_key=True, default=-1)
    per_insercion = models.CharField(max_length=20,default=-1)
    per_eliminar = models.CharField(max_length=20,default=-1)
    per_actualizar = models.CharField(max_length=20,default=-1)
    per_consultar = models.CharField(max_length=20,default=-1)
    fec_modificacion = models.DateTimeField(default=timezone.now)
    cod_rol = models.IntegerField(max_length=10)
    
    class Meta:
        db_table = 'seg_permisos'

#Donantes modelos 3
class Donantes(models.Model):
    cod_donantes = models.AutoField(primary_key=True, default=-1)
    cod_usuario = models.CharField(max_length=20,default=-1)
    nombre = models.CharField(max_length=100, default=-1)
    identidad = models.CharField(max_length=15, default=-1)
    direccion = models.CharField(max_length=50,default=-1)
    telefono = models.CharField(max_length=20,default=-1)
    email = models.CharField(max_length=50,default=-1)
    fec_creacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'donantes'

#Donaciones modelos 4
class Donaciones(models.Model):
    cod_donacion = models.AutoField(primary_key=True, default=-1)
    nom_institucion = models.CharField(max_length=40,default=-1)
    tip_donacion = models.CharField(max_length=40,default=-1)
    des_donacion = models.CharField(max_length=40,default=-1)
    fec_donacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'donaciones'

#AXE EVALUACION modelos 5
class AxeEvaluacion(models.Model):
    cod_evaluacion = models.AutoField(primary_key=True, default=-1)
    nom_institucion = models.CharField(max_length=40,default=-1)
    des_evaluacion = models.CharField(max_length=20,default=-1)
   
    class Meta:
        db_table = 'axe_evaluacion'

#USUARIOS modelos 6
class Usuarios(models.Model):
    cod_usuario = models.AutoField(primary_key=True, default=-1)
    nom_usuario = models.CharField(max_length=40,default=-1)
    contrasenia = models.CharField(max_length=20,default=-1)
    estado_usuario = models.BooleanField(max_length=20,default=-1)
    fec_creacion = models.DateTimeField(default=timezone.now)
    cod_rol = models.IntegerField(max_length=20,default=-1)
    telefono = models.CharField(max_length=15,default=-1)
    email = models.CharField(max_length=50,default=-1)

    class Meta:
        db_table = 'usuarios'

#Centro Educativo modelos 7
class Centro_Educativo(models.Model):
    cod_identificador = models.AutoField(primary_key=True, default=-1)
    cod_sace = models.CharField(max_length=40,default=-1)
    nom_institucion = models.CharField(max_length=20,default=-1)
    tip_categoria_institucion = models.CharField(max_length=40,default=-1)
    
    class Meta:
        db_table = 'centro_educativo'

#Recuperar Contrasenia 8
class Recuperar_Contrasenia(models.Model):
    cod_pregunta_respuesta = models.AutoField(primary_key=True, default=-1)
    cod_usuario = models.IntegerField(max_length=40,default=-1)
    nomb_pregunta = models.CharField(max_length=200,default=-1)
    des_respuesta = models.CharField(max_length=200,default=-1)
    
    class Meta:
        db_table = 'recuperar_contrasenia'
