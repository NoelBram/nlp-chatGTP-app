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

import os
import openai

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
        openai.organization = "org-YpgyJTbeI03z5AzIC1R0XSF7"
        openai.api_key = os.getenv("")

        prompt='Can you rewrite or reword the following text and condense it to be less than 1000 words while retaining its meaning and message? \'{i}\''.format(i = input_text)
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50
        )
        generated_text = response.choices[0].text
        print(generated_text)
        return {"response": generated_text}
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
