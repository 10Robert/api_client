from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields  = ['nome']
    search_fields = ['nome', 'id', 'cpf']     
    filterset_fields = ['ativo']

    
    @method_decorator(cache_page(60 * 2))
    def dispatch(self, *args, **kwargs):
        return super(ClientesViewSet, self).dispatch(*args, **kwargs)
