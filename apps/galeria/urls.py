from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, deletar_imagem, nova_imagem, editar_imagem

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/<int:foto_id>', imagem, name = 'imagem'),
    path("buscar", buscar, name='buscar'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('editar_imagem', editar_imagem, name='editar_imagem'),
    path('deletar_imagem', deletar_imagem, name='imagem_imagem'),
]