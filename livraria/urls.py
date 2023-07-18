from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias', views.CategoriaView.as_view()),
    path('categorias/<int:id>', views.CategoriaView.as_view())
]
