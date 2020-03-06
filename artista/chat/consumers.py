'''
V1 
'''

from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


'''
V2
'''
# import asyncio
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async
# from channels.generic.websocket import WebsocketConsumer
# import json


# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print("Conneted ", event)
#         await self.send({
#             "type" : "websocket.accept"
#         })

#         await self.send({
#             "type" : "websocket.send",
#             "text" : "Hello"
#         })

#     async def websocket_disconnect(self, event):
#         print("websocket_disconnect ", event)
#         pass

#     async def websocket_receive(self, event):
#         print("websocket_receive ", event)
    

'''
V3
'''
# chat/consumers.py
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# import json

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))