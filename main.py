import openai
import os
from googletrans import Translator
import json

openai.api_key = os.environ.get("OPENAI_API")


class chat_ai:
    def __init__(self):
        self.openai = openai
        self.translator = Translator()

    def respond(self, message, key):
        print(message)
        messages = open('data', 'r').read() + '\n' + message
        print(messages)
        res = self.openai.Completion.create(model="text-davinci-003", prompt=messages, temperature=0.9, max_tokens=300,
                                            top_p=1,
                                            frequency_penalty=0, presence_penalty=0.6)
        respond = res['choices'][0]['text']
        if key == 'km':
            return self.khmer_translation(respond)
        print(respond)
        return respond

    def khmer_translation(self, message):
        if 'My name' in message:
            return 'ខ្ញុំឈ្មោះ ពាវ មុន្នីវីរៈពេជ្រ'
        return self.translator.translate(message, dest='km').text

    def translation(self, message):
        detect_lange = self.detection_lang(message)
        if detect_lange == 'km':
            translate = self.translator.translate(message, dest='en').text
            print(translate)
            return self.respond(translate, detect_lange)
        return self.respond(message, detect_lange)

    def detection_lang(self, message):
        return self.translator.detect(message).lang

    def generate_image(self, message):
        response = self.openai.Image.create(
            prompt=message,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return f'<img src="{image_url}" alt="Girl in a jacket" width="200" height="350">'
