from django.urls import path

from . import consumers



websocke_urlpatterns = [
    path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
]

