import openai
import os
from googletrans import Translator
from richieV2 import Richie
openai.api_key = os.environ.get("OPENAI_API")


class RichieService:
    def __init__(self):
        self.openai = openai
        self.translator = Translator()

    def respond(self, message, key):
        session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..DEobbbOPUG8-8pv_.OrC6iUAoJ5I8wUvpIkqGmZCiWhp4HMODeNCqr7cMlqpLdP48DgAppnwOUgfeVENcvg7aerr6WybDgHgWE4RSaqCA13H7mziyG_Qxiaj8E0zXeMrsTPiOLrdC2bRGAQEUZ-mx1CTyBWtNxGfGIqjHDQMImJPxVSKzQUYk7_wfC-UTmiaKqXel58ZtMTPAIVwVPCMXZwyV65HREcoscHjjFMiOKezPwdJm-dz-PfXYbP4mK8Hoh7HF7vS82MK1s6-2PzaDsGSr7q3-N3-ua3T6aFJRZMlWVxJv5Ol0eX_ob8c1hEsZ_XLq3tPkhUa6a4PyB59rwl0FKX1Y3qT4yHtGgtaOIXgVnQY_5V7ygBe-eGPX4VZbf8j_z64nA2IL_A6Bk6I76mQn-OxUsW1mf_A8AXJXevbZwAaYXG8Bp24G6GBw7wSVPjvfy2OZFoAU3_rxG1Uc35jb79zxbPTqhiW3sNB1007Nvmjd_fmIxfVC7E_dHqpNpQ9Wr0laeLSd3pqrfE3XnCmDL9-F91xRv4GBpPWywSJW5CUZ7Jr1fah6QInk2xuF1OImOcHauHWCmmpbg1InRNckEQTxvo606eMILzm-kv7MZimgOzvEfG85xzkWW28HQu6dY8bMrU0c6rDAUX1Le5HwnS0APeGrM_f2kwueeqlHuSTMX7YaOP3x3lAmjqcpKPTrj3qZUJlKEumxZNc8sRnyOsU8HuspSM7aNkx8il41_9kQUyoeXLLLDPgBXNj3Ka9eT2bzN3vBY6jagBjA6w3IJ0x4UHgnNV-8ZHPlMn52kmKjuMK1PWyaQY7xUy-6V6lEAXsnujgeKgnXV2dtCQfAiqdG9HsBfSRxsD3KZmW-WFzDkhM6MUmRqUU8SapzgZlnYtVOPlq5UL72YCcACStvDJphG6fWVBykJ-X9DVociAw1NQl365T1PXhGs7ZxmNqavKtU8Cddqq9U2LdOHoE5LJImdFnZ6ZM1gr2HCaVFqvGv4jdpjk6qGIc8mdk8M_DgKGYDslAZK1vzKGFU4xWlLwF46YjFZMJjEubKMxeYogshAUzqbi9N-ZSBGFxThoZyjr7oI7DIriRJuaSfgjL0rDfLGe6D3c-cugDvWnRSZxsu2x8KDP1w4F-EpmLNkfADujHYqAXGAZ92-cZvMutBSRzqDujEWTtEc83RdLpOnVKZLeYDetlUOzomm46jT3GmN30fjO2-uTxabOcm7-N3pBmPU4SErHaudbPdnKSAtPfNJiOLkVxCCwT10ddaT9zwcB9F390drStMZwkzYX0YomQLMBYdsm5OrmOCfAX4fcGRCRmMSrM3_KtqrCobcrvRpNZ9boUWBd6rJ6GWzRHGRlzJM_kbyCWs78HnXxtwP_LeZO_GzIpHZ7ShW6_212cZiT92cvWDCZOX1wGOPH_krR_XEYHfFMdpKI5u4IZL7NG4l4Q7p63NUuqjUG9AqQG2dNLMA7WXd3RcpzGjJRUNs2skmS7TI6LW6USiIR8j_Cn3MmcRxjT_ZhGSIjNQY8-upyKlZozjVmnokdRbgWe8WljmpW-1w6Dw0EPy-D7TUJfUYfmv2vciG5r1FdKC44oViCramtx-iO9OEfTTqhaG0qrExMbJkV8Dl3nGlL23PBmtffAbg5G6n1d0OE8ygQKiCkHEuUc6W1zQnt_DaykhscNMhUC9MOizTxK3hOAaNoskzu81qfUD8jVSwHivGkysqf-qbHMOqfz5l6zxbOmjOsFzmc0DzfJctJz1Pr6HP8loPHRY-AJJSdFNWucrY2WQe8o50zaNGTNAN8ZW88M-HfphSp6GnTg-lX6j54mW0VSIcyO_HoeMvSBWEGUOvPrTIdKwH7GL7eQF6TFgQV93wAX9sr08-ohgA-f7pW0iU5gx-iZS_gyMbhXUvaqNaR8F19o2k9I9LpGMsV5YNvcn8WwbyZMy82Emh9XWtT0QP7jCFP2P3LJnqQ8gfzQcDVknRWLKacJCw-lNH6n2SdYMeD6tK2nWE-QPIE82okQMEY06B-YSr0lEZ042p2ys05cwfbey3Bxhd40Z7H1pZwLaR7uOWiM1uiKkJzqd78ZxMgOmsAxAqCqYOPLCR38FDgNPX_M6QWcuVRDPRZRsS8omFu6aIHLjOVPMlXaqsFCLBCWIaz9QM_HOrUTFE9gJgUlWrJ45fs6tQpRMUVO-sxeYveKYZTY3pDGbbx-uzgXTu-MkWIo4FJJTTry-TcUYEyQH39l9OIiEA20urMaAvEIABqBHNJGpDZl6mwieLfLGQokYKp7N39RwAFX9zTVwQAj6soPix47MlWtp1OgDMDWo9dZstvofFeOXB8AEF9lIsX4WF9zN3Jm9w7u1iZJKLXYkOzdvR7lK8sttwMhT1DiUlb2VEq05sVyg7ImrV0pooKmQdw8GReIQyaNQCPP7ZJNnf_7hLuCXJ42xY8H100g33nJpkW6LPKfXDsZYFkWAsS31Sv1hskSH2h0fPDqXeJOBYvIZElIPSGBGj8dWwP_RVb9uXHjT4OSnnQLCxAR9DYun_fH1je_F5pnU-XG8l8rUq4tZCtaHejwKM8N4Q2pfUM3EKNybWE-eucTFXwpLv8XRV7Gz6sMMriA2hEeWF44ct2OC8T7eHmk-okylthzygbbHfLMIxwiw5iMumLZECn7WHTzfC1AJJLEUWVg.yXbtD8sYxGQn89ycHX8zHA'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
        api = Richie(session_token)
        # conversation_id = 'e2d767e9-c105-4ce3-9c8e-4d4c518a9fbf'

        resp = api.send_message(f"""{message}""")
        respond = resp['message']

        if key == 'km':
            return self.khmer_translation(respond)
        else:
            return respond

        # res = self.openai.Completion.create(model="text-davinci-003", prompt=message, temperature=0.9, max_tokens=300,
        #                                     top_p=1,
        #                                     frequency_penalty=0, presence_penalty=0.6)
        # respond = res['choices'][0]['text']
        # if key == 'km':
        #     return self.khmer_translation(respond)
        # return respond

    def khmer_translation(self, message):
        if 'My name' in message:
            return 'ខ្ញុំឈ្មោះ ពាវ មុន្នីវីរៈពេជ្រ'
        return self.translator.translate(message, dest='km').text

    def translation(self, message):
        detect_lange = self.detection_lang(message)
        if detect_lange == 'km':
            translate = self.translator.translate(message, dest='en').text
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
