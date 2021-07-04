from django.urls import path

from .consumers import JokeConsumer

ws_urlpatterns = [
    path('ws/jokes/', JokeConsumer.as_asgi())
]