from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.usuarios_serializer import UsuariosSerializer
from rest_framework import status as status_code
from ..services import cidades_atendimento_service
from ..paginations import profissionais_localidade_pagination

class UsuariosView(APIView, profissionais_localidade_pagination.ProfissionaisLocalidadePagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        usuarios = cidades_atendimento_service.listar_prossionais_cidade(cep)
        usuarios_paginacao = self.paginate_queryset(usuarios, request)
        serializer_usuarios = UsuariosSerializer(usuarios_paginacao, many=True, context={'request': request})
        return self.get_paginated_response(serializer_usuarios.data)
    