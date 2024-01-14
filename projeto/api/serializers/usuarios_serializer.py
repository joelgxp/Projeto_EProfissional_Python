from datetime import date
from rest_framework import serializers
from ..models import Usuario
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

class UsuariosSerializer(serializers.ModelSerializer):
    
    cidade = serializers.SerializerMethodField()
    chave_pix = serializers.CharField(required=False)
    password_confirmation = serializers.CharField(write_only=True, required=True)
    tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)
    foto_de_perfil = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    password = serializers.CharField(write_only=True)
    foto_documento = serializers.ImageField(write_only=True, required=True)
    token = serializers.SerializerMethodField(required=False)
    
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
            'token',
            'foto_de_perfil',
            'cidade'
        )
        
    def get_token(self, user):
        token = RefreshToken.for_user(user)
        data = { 
            "refresh": str(token),
            "access": str(token.access_token),
        }
        return data
        
    def validate_password(self, password):
        password_confirmation = self.initial_data["password_confirmation"]
        if password != password_confirmation:
            raise serializers.ValidationError("As senhas precisam ser iguais.")
        return password
    
    def validate_nascimento(self, nascimento):
        data_atual = date.today()
        idade = data_atual.year - nascimento.year - (
            (data_atual.month, data_atual.day) < (nascimento.month, nascimento.day)
        )
        if idade < 18:
            raise serializers.ValidationError("O usuário deve ter mais de 18 anos.")
        if idade > 100:
            raise serializers.ValidationError("Idade maior que a permitida.")
        return nascimento
    
    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        validated_data.pop('password_confirmation', None)
        reputacao_geral = 2
        if validated_data['tipo_usuario'] == 2:
            reputacao_geral = Usuario.profissional_object.reputacao_geral()['reputacao__avg']
            if reputacao_geral is None:
                reputacao_geral = 5
        usuario = Usuario.objects.create(reputacao=reputacao_geral, **validated_data)
        return usuario
        
    def get_cidade(self, obj):
        return "Guaxupé"