from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Seg_Permisos, Seg_Roles,Donantes,Donaciones,Usuarios, AxeEvaluacion, Recuperar_Contrasenia,Centro_Educativo

class Seg_Roles_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Seg_Roles
        fields = '__all__'

class Seg_Permisos_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Seg_Permisos
        fields = '__all__'

class Donantes_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Donantes
        fields = '__all__'

class Donaciones_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Donaciones
        fields = '__all__'

class Usuarios_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class Centro_Educativo_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Centro_Educativo
        fields = '__all__'

class AxeEvaluacion_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = AxeEvaluacion
        fields = '__all__'

class Recuperar_Contrasenia_Seriealizers(serializers.ModelSerializer):
    class Meta:
        model = Recuperar_Contrasenia
        fields = '__all__'
