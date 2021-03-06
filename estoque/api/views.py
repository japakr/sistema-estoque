from rest_framework import generics
from estoque.models import Componente
from .serializers import ComponenteSerializer

class ComponenteAPIView(generics.ListAPIView): #RetrieveAPIView
    #lookup_field = 'id'
    serializer_class = ComponenteSerializer

    def get_queryset(self):
        return Componente.objects.order_by('nome')
