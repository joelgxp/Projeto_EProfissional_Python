from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers import usuarios_serializer
from rest_framework import status as status_code
from ..services import cidades_atendimento_service
from ..paginations import profissionais_localidade_pagination

class UsuariosView(APIView, profissionais_localidade_pagination.ProfissionaisLocalidadePagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        usuarios = cidades_atendimento_service.listar_prossionais_cidade(cep)
        usuarios_paginacao = self.paginate_queryset(usuarios, request)
        serializer_usuarios = usuarios_serializer.UsuariosSerializer(usuarios_paginacao, many=True, context={'request': request})
        return self.get_paginated_response(serializer_usuarios.data)
    
    def post(self, request, format=None):
        serializer_usuario = usuarios_serializer.UsuariosSerializer(data=request.data, context={'request': request})
        
        if serializer_usuario.is_valid():
            usuario_criado = serializer_usuario.save()
            serializer_usuario = usuarios_serializer.UsuariosSerializer(usuario_criado)
            return Response(serializer_usuario.data, status=status_code.HTTP_201_CREATED)
        return Response(serializer_usuario.errors, status=status_code.HTTP_400_BAD_REQUEST)
        
    