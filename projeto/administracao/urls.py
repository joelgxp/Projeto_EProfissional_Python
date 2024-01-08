from django.urls import path
from .views import servicos_views, usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('servicos/cadastrar', servicos_views.cadastrar_servico, name='cadastrar-servico'),
    path('servicos/listar', servicos_views.listar_servicos, name='listar-servicos'),
    path('servicos/editar/<int:id>', servicos_views.editar_servico, name='editar-servicos'),
    path('servicos/deletar/<int:id>', servicos_views.deletar_servico, name='deletar-servicos'),
    
    path('usuarios/cadastrar', usuarios_views.cadastrar_usuario, name='cadastrar-usuario'),
    path('usuarios/listar', usuarios_views.listar_usuarios, name='listar-usuario'),
    path('usuarios/editar/<int:id>', usuarios_views.editar_usuario, name='editar-usuario'),
    
    path('autenticacao/login', auth_views.LoginView.as_view(), name='logar-usuario'),
    path('autenticacao/logout', auth_views.LogoutView.as_view(), name='sair-usuario'),
    path('alterar_senha', auth_views.PasswordChangeView.as_view(), name='alterar-senha'),
    
]