import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator


import room.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dMessage.settings")

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 room.routing.websockets_urlpatterns
#             )
#         )
#     ),
# })
import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AttributeError(
#         URLRouter(
#             room.routing.websockets_urlpatterns
#         )
#     )
# })
