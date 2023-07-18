from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from core.models import Categoria, Editora, Autor, Livro

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