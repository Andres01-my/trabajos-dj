from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar todos los pedidos
    path('', views.lista_pedidos, name='listar_pedidos'),
#Ruta para crear un nuevo pedido
    path('crear/', views.crear_pedido, name='crear_pedido'),
    # Ruta para ver el detaller de un pedido específico
    path('<int:pk>/', views.ver_pedido, name='ver_pedido'),
    # Ruta para editar un pedido existente
    # URL: /pedidos/editar/5/
    path('editar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),
    # Ruta para eliminar un pedido existente
    path('eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),
]