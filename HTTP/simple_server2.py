
from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def hello_world():
    user_agent = request.headers.get('User-Agent')
    print('user agent = {}'.format(user_agent))
    return 'Hello world!'


app.run()