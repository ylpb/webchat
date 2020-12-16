from channels.routing import ProtocolTypeRouter,URLRouter
from django.conf.urls import url
from app01 import consumers

application = ProtocolTypeRouter({
    'websocket':URLRouter([
        # websocket相关的url与视图函数对应关系
        url(r'^chat/$',consumers.ChatConsumer)
    ])
})


