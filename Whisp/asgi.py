
import os

from django.core.asgi import get_asgi_application

from channels import AuthMiddlewareStack
from channels import ProtocolTypeRouter,URLRouter

import rooms.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Whisp.settings')

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            rooms.routing.websocket_urlpatterns
            )
        ),
})


