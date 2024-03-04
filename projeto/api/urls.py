from django.urls import path
from .views import usuario_view, me_view, inicio_view

urlpatterns = [
    path('', inicio_view.InicioView.as_view(), name='inicio'),
    path('usuarios/localidades', usuario_view.UsuariosView.as_view(), name='usuario-list'),
    path('usuarios', usuario_view.UsuariosView.as_view(), name='cadastrar-usuarios'),
    path('me', me_view.MeView.as_view(), name='me-list'),
]