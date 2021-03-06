from django.urls import path, re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    # path('ws/chat/<pk>/', ChatConsumer.as_asgi()),
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/(?P<auth>[^/]+)/$', ChatConsumer.as_asgi())
]
