import requests
import json
from rest_framework import serializers

from ..models import CidadesAtendimento

def buscar_cidades_cep(cep):
    
    response = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )

    if response.status_code == 400:
        raise serializers.ValidationError({"detail": "CEP inválido"})
    cidade_api = json.loads(response.content)
    if 'erro' in cidade_api:
        raise serializers.ValidationError({"detail": "CEP não encontrado"})

    return cidade_api

def listar_prossionais_cidade(cep):
    codigo_ibge = buscar_cidades_cep(cep) ['ibge']
    try:
        cidade = CidadesAtendimento.objects.get(codigo_ibge=codigo_ibge)
        return cidade.usuario.filter(tipo_usuario='L')
    except CidadesAtendimento.DoesNotExist:
        return []
        