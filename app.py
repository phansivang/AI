from flask import Flask, render_template, request
from main import chat_ai
from flask_sslify import SSLify

app = Flask(__name__, template_folder='templates')
sslify = SSLify(app)


@app.route('/')
def home():
    return render_template(str('index.html'))


@app.route("/get/respond", )
def get_bot_response():
    message = request.args.get('msg')
    return chat_ai().translation(message)


@app.route('/v1/message', methods=['GET'])
def get():
    request_data = request.get_json()
    message = request_data['message']
    return chat_ai().translation(message)


if __name__ == "__main__":
    app.run()
