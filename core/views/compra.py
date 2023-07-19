
from core.models import Compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer

from rest_framework.viewsets import ModelViewSet


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    # serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CompraSerializer
        return CriarEditarCompraSerializer
    # filter only the currentUser compras
    def  get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name='Administradores'):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)