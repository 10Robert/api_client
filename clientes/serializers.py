from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'cpf', 'rg', 'celular', 'ativo', 'foto']
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Numero de CPF invalido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não coloque numeros no nome, apenas caracteres alfabéticos'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O numero de digitos do rg deve ser igual a 9 digitos!'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O telefone deve conter 11 digitos, e seguir este modelo (11 91234-1234)'})
        return data
    
"""    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O numero de digitos do cpf deve ser igual a 11 digitos!")
        return cpf
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não coloque numeros no nome, apenas caracteres alfabéticos")
        return nome
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O numero de digitos do rg deve ser igual a 9 digitos!")   
        return rg
    
    def validate_celular_tamanho(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O telefone de conter 11 digitos")
        return celular"""

