from django.contrib import admin
from django.urls import path, include

from core import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'editora', views.EditoraViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'livro', views.LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/class', views.CategoriaView.as_view()),
    path('categorias/class', views.CategoriaView.as_view()),
    path('categorias/<int:id>', views.CategoriaView.as_view()),
    path('categorias/apiview', views.CategoriaList.as_view()),
    path('categorias/apiview/<int:id>', views.CategoriaDetail.as_view()),
    path('categorias/generics', views.CategoriaListGeneric.as_view()),
    path('categorias/generics/<int:id>', views.CategoriaDetailGeneric.as_view()),
    path('', include(router.urls))
]
