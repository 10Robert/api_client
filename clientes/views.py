from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields  = ['nome']
    search_fields = ['nome', 'id', 'cpf']     
    filterset_fields = ['ativo']
    http_method_names = ['get', 'post', 'head', 'options', 'patch', 'post', 'delete']
    
    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["example"] = 'this is in context now'
        return context
    
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        user = self.request.query_params.get('pk', "")
        
        if user != "" and user.isnumeric():
            qs = qs.filter(id=user)
            
        return qs
    
    def get_object(self):
        pk = self.kwargs.get('pk', "")
        
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
            
        )
        
        
        return super().create(request, *args, **kwargs)
    
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(ClientesViewSet, self).dispatch(*args, **kwargs)
