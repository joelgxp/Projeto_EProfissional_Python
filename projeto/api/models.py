from django.db import models

import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from localflavor.br.models import BRCPFField

def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return os.path.join('usuarios_fotos', filename)

def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return os.path.join('documentos_fotos', filename)

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('P', 'Profissional'),
        ('C', 'Cliente')
    )
    
    nome_completo = models.CharField(max_length=200, null=True, blank=False)
    cpf = BRCPFField(null=True, unique=True, blank=False)
    nascimento = models.DateField(null=True, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    celular = models.CharField(max_length=15, null=True, blank=False)
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES, null=True, blank=False)
    foto_de_perfil = models.ImageField(upload_to=nome_arquivo_foto, null=True, validators = [validate_image_file_extension, ])
    foto_documento = models.ImageField(upload_to=nome_arquivo_documento, null=True, validators=[validate_image_file_extension, ])    
    ativo = models.BooleanField(default=True)

class CidadesAtendimento(models.Model):
    codigo_ibge = models.IntegerField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, related_name='cidades_atendidas')