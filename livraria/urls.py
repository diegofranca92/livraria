from django.contrib import admin
from django.urls import path, include

from core import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'editora', views.EditoraViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'livro', views.LivroViewSet)
router.register(r'compra', views.CompraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('categorias/class', views.CategoriaView.as_view()),
    path('categorias/class', views.CategoriaView.as_view()),
    path('categorias/<int:id>', views.CategoriaView.as_view()),
    path('categorias/apiview', views.CategoriaList.as_view()),
    path('categorias/apiview/<int:id>', views.CategoriaDetail.as_view()),
    path('categorias/generics', views.CategoriaListGeneric.as_view()),
    path('categorias/generics/<int:id>', views.CategoriaDetailGeneric.as_view()),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
