from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
 
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .Seriealizers import UserTokenSerializer

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data= request.data, context = {'request':request})

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']

            if user.is_active:
                token, created = Token.objects.get_or_create(user = user) #Devuelve una instancia y un booleano(Si fue creado)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data, 
                        'message':'Inicio de sesión exitoso'
                    }, status= status.HTTP_201_CREATED)
                else:
                    """
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete() #Si quiere volver a iniciar sesion, deberemos eliminar el token
                    token, created = Token.objects.get_or_create(user = user)
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data, 
                        'message':'Inicio de session exitoso'
                    }, status=status.HTTP_201_CREATED)
                    """       
                    token.delete()
                    return Response({
                        'error':'Ya se ha iniciado sesion con este usuario :('
                    })

        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status= status.HTTP_400_BAD_REQUEST)

        return Response({'message':'Hola desde Response'}, status= status.HTTP_200_OK) 

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
           # print(request.GET.get('token'))
            print(token)
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user

                #Cerrando la session
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()

                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()
                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({
                    'token_message':token_message,
                    'session_message':session_message,
                }, status= status.HTTP_200_OK)
        
            return Response({
                'error':'No se ha encontrado un usuario con esas credenciales.'
            }, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({
                'error':'No se ha encontrado token en la peticion'
            }, status= status.HTTP_409_CONFLICT)
