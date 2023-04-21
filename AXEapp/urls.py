from django.urls import path
#from apps.users.api.api import UserAPIView
from .api import roles_api_view, rol_detalle_api_view,donantes_api_view, donantes_detalle_api_view
from .api import donaciones_api_view, donaciones_detalle_api_view,evaluacion_api_view, evaluacion_detalle_api_view
from .api import permisos_api_view, permiso_detalle_api_view, usuarios_api_view, usuarios_detalle_api_view
from .api import centro_educativo_api_view, centro_educativo_detalle_api_view, contrasenia_api_view, contrasenia_detalle_api_view

urlpatterns = [
    path('Roles/', roles_api_view, name='roles'),
    path('Roles/<int:pk>', rol_detalle_api_view, name='rol_detalle'),
    path('Donacion/', donaciones_api_view, name='donaciones'),
    path('Donacion/<int:pk>', donaciones_detalle_api_view, name='donaciones_detalle'),
    path('Permisos/', permisos_api_view, name='permisos'),
    path('Permisos/<int:pk>', permiso_detalle_api_view, name='permiso_detalle'),
    path('Centro Educativo/', centro_educativo_api_view, name='centro_educativo'),
    path('Centro Educativo/<int:pk>', centro_educativo_detalle_api_view, name='centro_educativo_detalle'),
    path('Donantes/', donantes_api_view, name='donantes'),
    path('Donantes/<int:pk>', donantes_detalle_api_view, name='donantes_detalle'),
    path('Evaluacion/', evaluacion_api_view, name='evaluacion'),
    path('Evaluacion/<int:pk>', evaluacion_detalle_api_view, name='evaluacion_detalle'),
    path('Usuarios/', usuarios_api_view, name='usuarios'),
    path('Usuarios/<int:pk>', usuarios_detalle_api_view, name='usuarios_detalle'),
    path('Recuperar_Contrasenia/', contrasenia_api_view, name='contrasenia'),
    path('Recuperar_Contrasenia/<int:pk>', contrasenia_detalle_api_view, name='contrasenia_detalle'),
    #path('usuario/', UserAPIView.as_view(), name='usuario_api')
]