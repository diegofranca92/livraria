from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from core.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class EditoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ('nome', 'site')


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total')
        depth = 2
    
    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ('livro', 'quantidade')

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')
    
    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)

        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ('id', 'status', 'total', 'usuario', 'itens')

    def get_status(self, instance):
        return instance.get_status_display()

class LivroDetailSerializer(ModelSerializer):
    # definir os campos a sere retornados
    # categoria = CharField(source='categoria.descricao')
    # editora = EditoraSerializer()
    editora = EditoraNestedSerializer()
    # autores = SerializerMethodField()
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1

    # Retornar só o nome do autor
    # def get_autores(self, instance):
    #     nomes_autores = []
    #     autores = instance.autores.get_queryset()
    #     for autor in autores:
    #         nomes_autores.append(autor.nome)
    #     return nomes_autores