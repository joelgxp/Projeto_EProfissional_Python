from rest_framework.views import APIView
from ..serializers import usuarios_serializer
from rest_framework.response import Response
from rest_framework import status as status_code
from rest_framework import permissions

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        serializer_usuario = usuarios_serializer.UsuariosSerializer(request.user, context={'request': request})
        return Response(serializer_usuario.data, status=status_code.HTTP_200_OK)
    
