
from rest_framework.response import Response #para responder
from .models import Seg_Roles, Donaciones, Seg_Permisos,Centro_Educativo, Donantes,AxeEvaluacion, Usuarios, Recuperar_Contrasenia
from .Seriealizers import Seg_Roles_Seriealizers, Donaciones_Seriealizers, Seg_Permisos_Seriealizers, Usuarios_Seriealizers
from .Seriealizers import Centro_Educativo_Seriealizers, Donantes_Seriealizers, AxeEvaluacion_Seriealizers, Recuperar_Contrasenia_Seriealizers
from rest_framework.decorators import api_view
from rest_framework import status

from django.db import connection


#API DE ROLES
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion

def roles_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        roles = Seg_Roles.objects.all() #todos los registros
        roles_serializer = Seg_Roles_Seriealizers(roles, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(roles_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        roles_serializer = Seg_Roles_Seriealizers(data= request.data)#
        
        cod_roles = request.data.get('cod_rol') #Extraemos el codigo del rol, para el que crearemos permosos
        tip_roles = request.data.get('tip_roles')

        if roles_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_ROLES('I', %s,%s)", [cod_roles,tip_roles])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Rol creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(roles_serializer.errors)       

        return Response({'message':'¡Error al ingresar Rol!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def rol_detalle_api_view(request, pk = None): #pk 2
    roles = Seg_Roles.objects.filter(cod_rol = pk).first()  
    if roles:
        if request.method == 'GET':

            roles_serializer = Seg_Roles_Seriealizers(roles)        

            return Response(roles_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_roles = request.data.get('cod_rol')

                #Llamamos el registro a modificar
                roles = Seg_Roles.objects.filter(cod_rol = cod_roles).first() 

                roles_serializer = Seg_Roles_Seriealizers(roles, data = request.data)
                if roles_serializer.is_valid():

                    cod_rol = request.data.get('cod_rol')
                    tip_roles = request.data.get('tip_roles') #no funcion
                   
                   

                    cursor = connection.cursor()                    
                    cursor.execute("SELECT SP_ROLES('U', %s, %s)", [cod_rol, tip_roles])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Rol actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(roles_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#API DE DONACIONES
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def donaciones_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        donaciones = Donaciones.objects.all() #todos los registros
        donaciones_serializer = Donaciones_Seriealizers(donaciones, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(donaciones_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        donaciones_serializer = Donaciones_Seriealizers(data= request.data)#
        
        cod_donacion = request.data.get('cod_donacion') 
        nom_institucion = request.data.get('nom_institucion')
        tip_donacion = request.data.get('tip_donacion')
        des_donacion = request.data.get('des_donacion')

        if donaciones_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_DONACIONES('I', %s,%s,%s,%s)", [cod_donacion,nom_institucion,tip_donacion,des_donacion])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Donacion creada correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(donaciones_serializer.errors)       

        return Response({'message':'¡Error al ingresar Donacion!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def donaciones_detalle_api_view(request, pk = None): #pk 2
    donaciones = Donaciones.objects.filter(cod_donacion = pk).first()  
    if donaciones:
        if request.method == 'GET':

            donaciones_serializer = Donaciones_Seriealizers(donaciones)        

            return Response(donaciones_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_donaciones = request.data.get('cod_donacion')

                #Llamamos el registro a modificar
                donaciones = Donaciones.objects.filter(cod_donacion = cod_donaciones).first() 

                donaciones_serializer = Donaciones_Seriealizers(donaciones, data = request.data)
                if donaciones_serializer.is_valid():

                    cod_donacion = request.data.get('cod_donacion') 
                    nom_institucion = request.data.get('nom_institucion')
                    tip_donacion = request.data.get('tip_donacion')
                    des_donacion = request.data.get('des_donacion')
                   

                    cursor = connection.cursor()                    
                    cursor.execute("SELECT sp_donaciones('U', %s,%s,%s,%s)", [cod_donacion,nom_institucion,tip_donacion,des_donacion])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Donacion actualizada correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(donaciones_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#API de SEG_PERMISOS
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def permisos_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        permisos = Seg_Permisos.objects.all() #todos los registros
        permisos_serializer = Seg_Permisos_Seriealizers(permisos, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(permisos_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        permisos_serializer = Seg_Permisos_Seriealizers(data= request.data)#
        
        cod_permisos = request.data.get('cod_permisos') 
        per_insercion = request.data.get('per_insercion')
        per_eliminar = request.data.get('per_eliminar')
        per_actualizar = request.data.get('per_actualizar')
        per_consultar = request.data.get('per_consultar')
        cod_rol = request.data.get('cod_rol')

        if permisos_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_PERMISOS('I', %s,%s,%s,%s,%s,%s)", [cod_permisos,per_insercion,per_eliminar,per_actualizar,per_consultar,cod_rol])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Permiso creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(permisos_serializer.errors)       

        return Response({'message':'¡Error al ingresar Permiso!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def permiso_detalle_api_view(request, pk = None): #pk 2
    permisos = Seg_Permisos.objects.filter(cod_permisos = pk).first()  
    if permisos:
        if request.method == 'GET':

            permisos_serializer = Seg_Permisos_Seriealizers(permisos)        

            return Response(permisos_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_permiso = request.data.get('cod_permisos')

                #Llamamos el registro a modificar
                permisos = Seg_Permisos.objects.filter(cod_permisos = cod_permiso).first() 

                permisos_serializer = Seg_Permisos_Seriealizers(permisos, data = request.data)
               
               
                if permisos_serializer.is_valid():
                    
                 cod_permisos = request.data.get('cod_permisos') 
                 per_insercion = request.data.get('per_insercion')
                 per_eliminar = request.data.get('per_eliminar')
                 per_actualizar = request.data.get('per_actualizar')
                 per_consultar = request.data.get('per_consultar')
                 cod_rol = request.data.get('cod_rol')

                cursor = connection.cursor()                    
                cursor.execute("SELECT SP_PERMISOS('U', %s,%s,%s,%s,%s,%s)", [cod_permisos,per_insercion,per_eliminar,per_actualizar,per_consultar,cod_rol])
                cursor.close() #para cerrar la conexion a base de dato
                    
                return Response({'message':'¡Permiso actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
        else:
                  return Response(permisos_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#API DE CENTRO EDUCATIVO
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def centro_educativo_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        centro = Centro_Educativo.objects.all() #todos los registros
        centro_serializer = Centro_Educativo_Seriealizers(centro, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(centro_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        centro_serializer = Centro_Educativo_Seriealizers(data= request.data)#
        
        cod_identificador = request.data.get('cod_identificador') 
        cod_sace = request.data.get('cod_sace')
        nom_institucion = request.data.get('nom_institucion')
        tip_categoria_institucion = request.data.get('tip_categoria_institucion')
       
        if centro_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_CENTRO_EDUCATIVO('I', %s,%s,%s,%s)", [cod_identificador,cod_sace,nom_institucion,tip_categoria_institucion])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Centro Educativo creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(centro_serializer.errors)       

        return Response({'message':'¡Error al ingresar Centro Educativo!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def centro_educativo_detalle_api_view(request, pk = None): #pk 2
    centro = Centro_Educativo.objects.filter(cod_identificador = pk).first()  
    if centro:
        if request.method == 'GET':

            centro_serializer = Centro_Educativo_Seriealizers(centro)        

            return Response(centro_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_identicar = request.data.get('cod_identificador')

                #Llamamos el registro a modificar
                centro = Centro_Educativo.objects.filter(cod_identificador = cod_identicar).first() 

                centro_serializer = Centro_Educativo_Seriealizers(centro, data = request.data)
               
               
                if centro_serializer.is_valid():
                    
                   cod_identificador = request.data.get('cod_identificador') 
                   cod_sace = request.data.get('cod_sace')
                   nom_institucion = request.data.get('nom_institucion')
                   tip_categoria_institucion = request.data.get('tip_categoria_institucion')

                cursor = connection.cursor()                    
                cursor.execute("SELECT SP_CENTRO_EDUCATIVO('U', %s,%s,%s,%s)", [cod_identificador,cod_sace,nom_institucion,tip_categoria_institucion])
                cursor.close() #para cerrar la conexion a base de dato
                    
                return Response({'message':'¡Centro Educativo actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
        else:
                  return Response(centro_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#API DONANTES
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def donantes_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        donantes = Donantes.objects.all() #todos los registros
        donantes_serializer = Donantes_Seriealizers(donantes, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(donantes_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        donantes_serializer = Donantes_Seriealizers(data= request.data)#
        
        cod_donantes = request.data.get('cod_donantes') 
        cod_usuario = request.data.get('cod_usuario')
        nombre = request.data.get('nombre')
        identidad = request.data.get('identidad')
        direccion = request.data.get('direccion')
        telefono = request.data.get('telefono')
        email = request.data.get('email')

        if donantes_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_DONANTES('I', %s,%s,%s,%s,%s,%s,%s)", [cod_donantes,cod_usuario,nombre,identidad,direccion,telefono,email])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Donante creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(donantes_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def donantes_detalle_api_view(request, pk = None): #pk 2

    donantes = Donantes.objects.filter(cod_donantes = pk).first()  
    if donantes:
        if request.method == 'GET':

            donantes_serializer = Donantes_Seriealizers(donantes)        

            return Response(donantes_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_donante = request.data.get('cod_donantes')

                #Llamamos el registro a modificar
                donantes = Donantes.objects.filter(cod_donantes = cod_donante).first() 

                donantes_serializer = Donantes_Seriealizers(donantes, data = request.data)
                if donantes_serializer.is_valid():

                    cod_donantes = request.data.get('cod_donantes') 
                    cod_usuario = request.data.get('cod_usuario')
                    nombre = request.data.get('nombre')
                    identidad = request.data.get('identidad')
                    direccion = request.data.get('direccion')
                    telefono = request.data.get('telefono')
                    email = request.data.get('email')
                   

                    cursor = connection.cursor()                    
                    cursor.execute("SELECT SP_DONANTES('U', %s,%s,%s,%s,%s,%s,%s)", [cod_donantes,cod_usuario,nombre,identidad,direccion,telefono,email])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Rol actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(donantes_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
                
#API DE AXE EVALUACION
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def evaluacion_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        evaluacion = AxeEvaluacion.objects.all() #todos los registros
        evaluacion_serializer = AxeEvaluacion_Seriealizers(evaluacion, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(evaluacion_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        evaluacion_serializer = AxeEvaluacion_Seriealizers(data= request.data)#
        
        cod_evaluacion = request.data.get('cod_evaluacion') 
        nom_institucion = request.data.get('nom_institucion')
        des_evaluacion = request.data.get('des_evaluacion')

        if evaluacion_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_AXE_EVALUACION('I', %s,%s,%s)", [cod_evaluacion,nom_institucion,des_evaluacion])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Evaluacion creada correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(evaluacion_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def evaluacion_detalle_api_view(request, pk = None): #pk 2
    evaluacion = AxeEvaluacion.objects.filter(cod_evaluacion = pk).first()  
    if evaluacion:
        if request.method == 'GET':

            evaluacion_serializer = AxeEvaluacion_Seriealizers(evaluacion)        

            return Response(evaluacion_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_evaluaciones = request.data.get('cod_evaluacion')

                #Llamamos el registro a modificar
                evaluacion = AxeEvaluacion.objects.filter(cod_evaluacion = cod_evaluaciones).first() 

                evaluacion_serializer = AxeEvaluacion_Seriealizers(evaluacion, data = request.data)
                if evaluacion_serializer.is_valid():

                       cod_evaluacion = request.data.get('cod_evaluacion') 
                       nom_institucion = request.data.get('nom_institucion')
                       des_evaluacion = request.data.get('des_evaluacion')
                   

                       cursor = connection.cursor()                    
                       cursor.execute("SELECT SP_AXE_EVALUACION('U', %s,%s,%s)", [cod_evaluacion,nom_institucion,des_evaluacion])
                       cursor.close() #para cerrar la conexion a base de dato
                    
                       return Response({'message':'¡Evaluacion actualizada correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(evaluacion_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#API DE USUARIOS
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def usuarios_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        usuarios = Usuarios.objects.all() #todos los registros
        usuarios_serializer = Usuarios_Seriealizers(usuarios, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(usuarios_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        usuarios_serializer = Usuarios_Seriealizers(data= request.data)#
        
        cod_usuario = request.data.get('cod_usuario') 
        nom_usuario = request.data.get('nom_usuario')
        contrasenia = request.data.get('contrasenia')
        estado_usuario = request.data.get('estado_usuario')
        cod_rol = request.data.get('cod_rol')
        telefono = request.data.get('telefono')
        email = request.data.get('email')
        
        if usuarios_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_USUARIOS('I', %s,%s,%s,%s,%s,%s,%s)", [cod_usuario,nom_usuario,contrasenia,estado_usuario,cod_rol,telefono,email])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Usuario creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(usuarios_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def usuarios_detalle_api_view(request, pk = None): #pk 2
    usuarios = Usuarios.objects.filter(cod_usuario = pk).first()  
    if usuarios:
        if request.method == 'GET':

            usuarios_serializer = Usuarios_Seriealizers(usuarios)        

            return Response(usuarios_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_usuarios = request.data.get('cod_usuario')

                #Llamamos el registro a modificar
                usuarios = Usuarios.objects.filter(cod_usuario = cod_usuarios).first() 

                usuarios_serializer = Usuarios_Seriealizers(usuarios, data = request.data)
                if usuarios_serializer.is_valid():

                      cod_usuario = request.data.get('cod_usuario') 
                      nom_usuario = request.data.get('nom_usuario')
                      contrasenia = request.data.get('contrasenia')
                      estado_usuario = request.data.get('estado_usuario')
                      cod_rol = request.data.get('cod_rol')
                      telefono = request.data.get('telefono')
                      email = request.data.get('email')
                   

                      cursor = connection.cursor()                    
                      cursor.execute("SELECT SP_USUARIOS('U', %s,%s,%s,%s,%s,%s,%s)", [cod_usuario,nom_usuario,contrasenia,estado_usuario,cod_rol,telefono,email])
                      cursor.close() #para cerrar la conexion a base de dato
                    
                      return Response({'message':'¡Usuario actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(usuarios_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#API DE RECUPERAR CONTRASEÑA
@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def contrasenia_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        contrasenia = Recuperar_Contrasenia.objects.all() #todos los registros
        contrasenia_serializer = Recuperar_Contrasenia_Seriealizers(contrasenia, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(contrasenia_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        #request.data['cod_roles']  #
        contrasenia_serializer = Recuperar_Contrasenia_Seriealizers(data= request.data)#
        
        cod_pregunta_respuesta = request.data.get('cod_pregunta_respuesta') 
        cod_usuario = request.data.get('cod_usuario')
        nomb_pregunta = request.data.get('nom_pregunta')
        des_respuesta = request.data.get('des_respuesta')

        if contrasenia_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()
           cursor.execute("SELECT SP_RECUPERAR_CONTRASENIA('I', %s,%s,%s,%s)", [cod_pregunta_respuesta,cod_usuario,nomb_pregunta,des_respuesta])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Contraseña Recuperdad creada correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(contrasenia_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def contrasenia_detalle_api_view(request, pk = None): #pk 2
    contrasenia = Recuperar_Contrasenia.objects.filter(cod_pregunta_respuesta = pk).first()  
    if contrasenia:
        if request.method == 'GET':

            contrasenia_serializer = Recuperar_Contrasenia_Seriealizers(contrasenia)        

            return Response(contrasenia_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                cod_pregunta_respuestas = request.data.get('cod_pregunta_respuesta')

                #Llamamos el registro a modificar
                contrasenia = Recuperar_Contrasenia.objects.filter(cod_pregunta_respuesta = cod_pregunta_respuestas).first() 

                contrasenia_serializer = Recuperar_Contrasenia_Seriealizers(contrasenia, data = request.data)
                if contrasenia_serializer.is_valid():

                       cod_pregunta_respuesta = request.data.get('cod_pregunta_respuesta') 
                       cod_usuario = request.data.get('cod_usuario')
                       nom_pregunta = request.data.get('nom_pregunta')
                       des_respuesta = request.data.get('des_respuesta')
                   

                       cursor = connection.cursor() 
                       cursor.execute("SELECT SP_RECUPERAR_CONTRASENIA('U', %s,%s,%s,%s)", [cod_pregunta_respuesta,cod_usuario,nom_pregunta,des_respuesta])                
                       cursor.close() #para cerrar la conexion a base de dato
                    
                       return Response({'message':'¡Recuperacion actualizada correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(contrasenia_serializer.errors, status= status.HTTP_400_BAD_REQUEST)