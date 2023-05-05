from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Seg_Permisos, Seg_Roles,Donantes,Donaciones,Usuarios, AxeEvaluacion, Recuperar_Contrasenia,Centro_Educativo, User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #Indica que serializaremos todos los campos, podriamos incluir solo unos o excluir algunos

    def create(self, validated_data):
        user = User(**validated_data) #Le pasamos la informacion recibida
        user.set_password(validated_data['password']) #Establecemos la contraseña
        user.save() #Guardamos el usuario nuevo
        return user
    
    #Este metodo ha sido creado para encriptar las contraseñas que no estaban encriptadas
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


        #Este metodo se encargara de pintar en un diccionario los campos que hayamos solicitado
class UserListSerializer(serializers.ModelSerializer):
    #('id', 'username', 'email', 'password')
    def to_representation(self, instance):
        return {
            'id':instance['id'],
            'username':instance['username'], 
            'email':instance['email'], 
            'password':instance['password']
        }

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')
