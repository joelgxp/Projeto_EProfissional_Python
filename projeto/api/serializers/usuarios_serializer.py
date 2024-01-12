from rest_framework import serializers
from ..models import Usuario
from django.contrib.auth.hashers import make_password

class UsuariosSerializer(serializers.ModelSerializer):
    
    cidade = serializers.SerializerMethodField()
    chave_pix = serializers.CharField(required=False)
    password_confirmation = serializers.CharField(write_only=True, required=True)
    tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)
    foto_de_perfil = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    password = serializers.CharField(write_only=True)
    foto_documento = serializers.ImageField(write_only=True, required=True)
    
    class Meta:
        model = Usuario
        fields = (
            'nome_completo', 
            'cpf',
            'nascimento',
            'foto_documento',
            'celular', 
            'tipo_usuario',
            'chave_pix',
            'password',
            'password_confirmation',
            'email',
            'foto_de_perfil',
            'cidade'
        )
        
    def validate_password(self, password):
        password_confirmation = self.initial_data["password_confirmation"]
        if password != password_confirmation:
            raise serializers.ValidationError("As senhas precisam ser iguais.")
        return password
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        
    def get_cidade(self, obj):
        return "Guaxupé"