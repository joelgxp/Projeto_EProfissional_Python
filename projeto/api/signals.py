from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Usuario

def usuario_cadastrado(sender, instance, created, **kwargs):
    if created:
        assunto = 'Bem vindo'
        corpo_email = 'Seja bem vindo ao sistema'
        email_destino = [instance.email, ]
        email_remetente = 'joel@joelsouza.com.br'
        mensagem_html = render_to_string('email_cadastro.html', {'usuario': instance})
        send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=mensagem_html)
    
# post_save.connect(usuario_cadastrado, sender=Usuario)