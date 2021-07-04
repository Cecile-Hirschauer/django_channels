from channels.generic.websocket import AsyncWebsocketConsumer

class JokeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.add_group('jokes', self.channel_name)
        await self.accept()
        
    async def disconnect(self):
        await self.channel_layer.discard_group('jokes', self.channel_name)
    
    async def send_jokes(self, event):
        text_message = event['text']
        
        await self.send(text_message)