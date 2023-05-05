from django.db import models
from django.utils import timezone


#Login
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


#Seguridad Roles modelos 1
class Seg_Roles(models.Model):
    cod_rol = models.AutoField(primary_key=True, default=-1)
    tip_roles = models.CharField(max_length=20,default=-1)
    
    class Meta:
        managed = False
        db_table = 'seg_roles'
        #managed = False
        

#Seguridad Permisos modelos 2
class Seg_Permisos(models.Model):
    cod_permisos = models.AutoField(primary_key=True, default=-1)
    per_insercion = models.CharField(max_length=20,default=-1)
    per_eliminar = models.CharField(max_length=20,default=-1)
    per_actualizar = models.CharField(max_length=20,default=-1)
    per_consultar = models.CharField(max_length=20,default=-1)
    fec_modificacion = models.DateTimeField(default=timezone.now)
    cod_rol = models.IntegerField()
    
    class Meta:
        db_table = 'seg_permisos'
        managed = False
        

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
        managed = False

#Donaciones modelos 4
class Donaciones(models.Model):
    cod_donacion = models.AutoField(primary_key=True, default=-1)
    nom_institucion = models.CharField(max_length=40,default=-1)
    tip_donacion = models.CharField(max_length=40,default=-1)
    des_donacion = models.CharField(max_length=40,default=-1)
    fec_donacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'donaciones'
        managed = False
        

#AXE EVALUACION modelos 5
class AxeEvaluacion(models.Model):
    cod_evaluacion = models.AutoField(primary_key=True, default=-1)
    nom_institucion = models.CharField(max_length=40,default=-1)
    des_evaluacion = models.CharField(max_length=20,default=-1)
   
    class Meta:
        db_table = 'axe_evaluacion'
        managed = False
        


#USUARIOS modelos 6
class Usuarios(models.Model):
    cod_usuario = models.AutoField(primary_key=True, default=-1)
    nom_usuario = models.CharField(max_length=40,default=-1)
    contrasenia = models.CharField(max_length=20,default=-1)
    estado_usuario = models.BooleanField(max_length=20,default=-1)
    fec_creacion = models.DateTimeField(default=timezone.now)
    cod_rol = models.IntegerField()
    telefono = models.CharField(max_length=15,default=-1)
    email = models.CharField(max_length=50,default=-1)

    class Meta:
        db_table = 'usuarios'
        managed = False
        

#Centro Educativo modelos 7
class Centro_Educativo(models.Model):
    cod_identificador = models.AutoField(primary_key=True, default=-1)
    cod_sace = models.CharField(max_length=40,default=-1)
    nom_institucion = models.CharField(max_length=20,default=-1)
    tip_categoria_institucion = models.CharField(max_length=40,default=-1)
    
    class Meta:
        db_table = 'centro_educativo'
        managed = False
        

#Recuperar Contrasenia 8
class Recuperar_Contrasenia(models.Model):
    cod_pregunta_respuesta = models.AutoField(primary_key=True, default=-1)
    cod_usuario = models.IntegerField()
    nomb_pregunta = models.CharField(max_length=200,default=-1)
    des_respuesta = models.CharField(max_length=200,default=-1)
    
    class Meta:
        db_table = 'recuperar_contrasenia'
        managed = False
    
    


#-----------------
class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
