from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

consumer_obj_list = []

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        """请求websocket链接的时候自动触发"""
        # print('请求链接')
        self.accept()  # 与客户端建立链接
        consumer_obj_list.append(self)
    def websocket_receive(self, message):
        """前端浏览器发送消息自动触发"""
        print(message)  # 消息字典  {'type': 'websocket.receive', 'text': 'hahahaha'}
        # 给客户端发消息
        msg = message.get('text')
        for obj in consumer_obj_list:
            obj.send(text_data=msg)

    def websocket_disconnect(self, message):
        """断开websocket链接自动触发"""
        # print('断开链接')
        raise StopConsumer