from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Cliente
from rest_framework import status

class ClienteTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cliente-list')
        self.cliente1 = Cliente.objects.create(
            id = '4',
            nome = 'Robert',
            email = 'Robertlucasmtz124@gmail.com',
            cpf = '530.572.420-14',
            rg = '192210828',
            celular = '11 93266-9729',
            ativo = 'False',
        )
        
        
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisiçãop GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK) 
        
    def test_requisicao_post_para_criar_cliente(self):
        """Teste para verificar requisicao post, para criar cliente"""
        data = {
            'id': '10',
            'nome': 'Robert',
            'email': 'Robertlucasmtz124@gmail.com',
            'cpf': '256.513.150-04',
            'rg': '192210828',
            'celular': '11 93266-9729',
            'ativo': 'False',
        }
        response = self.client.post(self.list_url, data=data)
        
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_para_deletar_cliente(self):
        """Teste para verificar requisicao delete, para deletar cliente"""
        
        response = self.client.delete('/clientes/4')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_atualizar_endpoint_do_cliente(self):
        """Teste para verificar requisicao patch, para atualizar algum endpoint"""
        data = {
            'nome': 'Robert',
            'email': 'Robertlucasmtz124@gmail.com',
            'cpf': '618.277.850-47',
            'rg': '192210828',
            'celular': '11 93266-9729',
            'ativo': 'False',
        }
        
        response = self.client.patch('/clientes/4', data=data)
        
        self.assertEquals(response.status_code, status.HTTP_200_OK)