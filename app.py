from flask import Flask, render_template, request
from main import Chat_AI

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template(str('index.html'))


@app.route("/get/respond", )
def get_bot_response():
    message = request.args.get('msg')
    return Chat_AI().translation(message)


@app.route('/v1/message', methods=['GET'])
def get():
    request_data = request.get_json()
    message = request_data['message']
    return Chat_AI().translation(message)


if __name__ == "__main__":
    app.run(debug=True)
