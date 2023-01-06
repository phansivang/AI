from flask import Flask, render_template, request, Response
from main import chat_ai
from flask_sslify import SSLify
import os

app = Flask(__name__, template_folder='templates')
sslify = SSLify(app)
ips =  [os.environ.get("IPSLIST")]

@app.route('/')
def home():
    return render_template(str('index.html'))

@app.before_request
def block_ip():

  if request.remote_addr in ips:
    return Response("Not allowed IP", status=403)

@app.route("/get/respond", )
def get_bot_response():
    message = request.args.get('msg')
    print('IP address' + request.remote_addr)
    return chat_ai().translation(message)


@app.route('/v1/message', methods=['GET'])
def get():
    request_data = request.get_json()
    message = request_data['message']
    return chat_ai().translation(message)


if __name__ == "__main__":
    app.run()
