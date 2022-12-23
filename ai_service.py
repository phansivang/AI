import openai
import os
from googletrans import Translator

openai.api_key = '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'

message_code = ['code', 'python', 'javascript', 'c++', 'node js', 'php', 'c#', 'name']


class Chat_AI:
    def __init__(self):
        self.openai = openai
        self.translator = Translator()

    def respond(self, message, key):
        res = self.openai.Completion.create(model="text-davinci-003", prompt=message, temperature=0.9, max_tokens=150,
                                            top_p=1,
                                            frequency_penalty=0, presence_penalty=0.6, stop=['Human:', 'AI:'])
        respond = res['choices'][0]['text']
        if key == 'km':
            return self.khmer_translation(respond)
        if self.ai_info(respond):
            return  self.ai_info(respond)
        return respond

    def khmer_translation(self, message):
        print(message)
        if 'My name'  in message:
            return self.ai_info(message)
        return self.translator.translate(message, dest='km')

    def translation(self,message):
        detect_lange =  self.detection_lang(message)
        if detect_lange == 'km':
            translate =  self.translator.translate(message, dest='en')
            return  self.respond(translate, detect_lange)
        return self.respond(message, detect_lange)

    def detection_lang(self, message):
        return  self.translator.detect(message)

    def ai_info(self, res):
        info = 'My name is Peav monivireak pech, AKA Richie, and I am a full-stack developer currently studying computer science at CADT and fintech at TGI.'
        if self.detection_lang(res) == 'en':
            if 'My name' in res:
                return  info
        pass

    def greeting_validation(self, message):
        key_words = ['hello ', 'hi ', 'What up ', "What's up ", 'Hey ']
        for key_word in key_words:
            if message in key_word:
                if self.detection_lang(message) == 'km':
                    return message.__add__('លោក')
                return message.__add__('Bot')
        pass