from stream_chat import StreamChat
import os

class chat:
    def __init__(self):
        self.chat = StreamChat(api_key=os.environ.get('API_KEY'), api_secret=os.environ.get('API_SECRET'))

    def channel(self):
        return self.chat.channel('messaging', channel_id='richiiechat')

    def send_message(self,message: dict , id: str):
        return self.channel().send_message(message, user_id=id)

    def message_formate(self, message: dict, user_id: str):
        messages = {
            "text": message,
            "attachments": [{
                "type": 'image',
                "asset_url": 'https://bit.ly/2K74TaG',
                "thumb_url": 'https://bit.ly/2Uumxti',
                "myCustomField": 123
            }],
            "mentioned_users": [user_id],
            "anotherCustomField": 234,
        }
        return messages