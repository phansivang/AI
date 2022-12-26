import openai
import os
from googletrans import Translator
import json

openai.api_key = os.environ.get("OPENAI_API")


# message_code = ['code', 'pytho', 'javascript', 'c++', 'node js', 'php', 'c#', 'nname']

class Chat_AI:
    def __init__(self):
        self.openai = openai
        self.translator = Translator()
        self.json = json.load(open('data.json', encoding="utf8"))

    def respond(self, message, key):
        res = self.openai.Completion.create(model="text-davinci-003", prompt=message, temperature=0.9, max_tokens=300,
                                            top_p=1,
                                            frequency_penalty=0, presence_penalty=0.6, stop=['Human:', 'AI:'])
        respond = res['choices'][0]['text']
        if key == 'km':
            return self.khmer_translation(respond)
        if self.check_ai_name(respond, key): return self.check_ai_name(respond, key)
        return respond

    def khmer_translation(self, message):
        if 'My name' in message:
            return self.json['data']['nameKh']
        return self.translator.translate(message, dest='km').text

    def translation(self, message):
        greeting = self.greeting_validation(message)
        detect_lange = self.detection_lang(greeting)
        if detect_lange == 'km':
            translate = self.translator.translate(greeting, dest='en').text
            return self.respond(translate, detect_lange)
        return self.respond(greeting, detect_lange)

    def detection_lang(self, message):
        return self.translator.detect(message).lang

    def check_ai_name(self, res, key):
        info = self.json
        if 'My name' in res:
            if key == 'en':
                return info['data']['nameEn']

    def greeting_validation(self, message):
        key_words = ['hello ', 'hi', 'what up ', "what's up ", 'hey','សួស្ដី','សួស្ដីបង','ហាយ','ហេឡូ','បង']
        for key_word in key_words:
            if str(message).lower() in key_word:
                return 'Hello madam?'
            pass
        return message