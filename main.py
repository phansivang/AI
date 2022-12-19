from flask import Flask, render_template, request
from ai_service import Chat_AI
import openai

class AI_Chat:
    def __init__(self):
        self.app = Flask(__name__, template_folder='templates')

        @self.app.route('/')
        def home():
            return render_template(str('index.html'))

        @self.app.route("/get")
        def get_bot_response():
            message = request.args.get('msg')
            return Chat_AI().translation(message)

if __name__ == "__main__":
    AI_Chat().app.run()