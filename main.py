import openai
import os
from googletrans import Translator

openai.api_key = os.environ.get("OPENAI_API")


# message_code = ['code', 'pytho', 'javascript', 'c++', 'node js', 'php', 'c#', 'nname']


class Chat_AI:
    def __init__(self):
        self.openai = openai
        self.translator = Translator()

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
            return 'នាងខ្ញុំឈ្មោះ ពាវ មុនីវីរៈពេជ្រ'
        return self.translator.translate(message, dest='km').text

    def translation(self, message):
        detect_lange = self.detection_lang(message)
        if detect_lange == 'km':
            translate = self.translator.translate(message, dest='en').text
            return self.respond(translate, detect_lange)
        return self.respond(message, detect_lange)

    def detection_lang(self, message):
        return self.translator.detect(message).lang

    def check_ai_name(self, res, key):
        info = 'My name is Peav monivireak pech, AKA Richie, and I am a full-stack developer currently studying ' \
               'computer science at CADT and fintech at TGI. '
        if 'My name' in res:
            if key == 'en':
                return info

    def greeting_validation(self, message):
        key_words = ['hello ', 'hi ', 'What up ', "What's up ", 'Hey ']
        for key_word in key_words:
            if message in key_word:
                if self.detection_lang(message) == 'km':
                    return message.__add__('លោក')
                return message.__add__('Bot')
        pass
