from django.apps import AppConfig #importa la clase AppConfig de django.apps


class PedidosConfig(AppConfig):   #define la configuración de la aplicación "pedidos"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pedidos'

