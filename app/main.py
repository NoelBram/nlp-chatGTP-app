# Flask imports
import requests
from flask import Flask, render_template, request
from flask_socketio import SocketIO

# Data processing imports
import warnings

# Plotting imports
import matplotlib
matplotlib.use('Agg')

from threading import Lock

from chatGTP_wrapper import *

# Suppress warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

sio = SocketIO(app)

thread = None
thread_lock = Lock()

@app.route('/')
@app.route('/index', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        input_text = request.json["input_text"]
        bot = ChatGPT()
        response = bot.ask('Can you rewrite or reword the following text and condense it to 1000 words or less while retaining its meaning and message? \'{i}\''.format(i = input_text))
        response = str(response)
        # bot.clear_history() # clear the history/context of the ChatGPT instance
        print(response)
        return {"response": response}
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
