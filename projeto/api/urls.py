from django.urls import path
from .views import usuarios_view

urlpatterns = [
    path('usuarios/localidades', usuarios_view.UsuariosView.as_view(), name='listar-usuarios-list'),
    path('usuarios', usuarios_view.UsuariosView.as_view(), name='cadastrar-usuarios'),
]