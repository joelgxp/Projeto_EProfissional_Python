from rest_framework import serializers
from ..models import Usuario

class UsuariosSerializer(serializers.ModelSerializer):
    
    cidade = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'cpf', 'celular', 'cidade')
        
    def get_cidade(self, obj):
        return "Guaxupé"