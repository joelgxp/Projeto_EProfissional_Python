from django.urls import path
from django.urls.base import reverse_lazy
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
    path('alterar_senha', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('listar-servicos')), name='alterar-senha'),
    path('resetar_senha', auth_views.PasswordResetView.as_view(), name='resetar-senha'),
    path('resetar_senha/sucesso', auth_views.PasswordResetDoneView.as_view(), name='resetar-senha-sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), name='resetar-senha-confirmar'),
    path('resetar_senha/feito', auth_views.PasswordResetDoneView.as_view(), name='resetar-senha-completo'),
    
]