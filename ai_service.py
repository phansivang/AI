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
        return respond

    def khmer_translation(self, message):
        return self.translator.translate(message, dest='km')

    def translation(self,message):
        detect_lange =  self.detection_lang(message)
        if detect_lange == 'km':
            translate =  self.translator.translate(message, dest='en')
            return  self.respond(translate, detect_lange)
        return self.respond(message, detect_lange)

    def detection_lang(self, message):
        return  self.translator.detect(message)

