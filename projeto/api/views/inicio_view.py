from django.urls.base import reverse
from rest_framework.views import APIView
from ..hateoas import Hateoas
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status as status_code

class InicioView(APIView):
    def get(self, request, format=None):
        links = Hateoas()
        links.add_get('self', reverse('inicio'))
        links.add_get('login', reverse('token_obtain_pair'))
        links.add_get('logout', reverse('logout-list'))
        links.add_get('usuario_logado', reverse('me-list'))
        links.add_get('cadastrar_usuario', reverse('usuario-list'))
        return Response({"links": links.to_array()}, status=status_code.HTTP_200_OK)