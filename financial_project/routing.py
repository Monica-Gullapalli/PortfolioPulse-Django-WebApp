# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from django.core.asgi import get_asgi_application
# from channels.middleware import ProtocolTypeRouter, AuthMiddlewareStack
# from analyzer_app import views

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 [path("plot_graph/", views.plot_graph)]
#             )
#         ),
#     }
# )