# Flask imports
import requests
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import subprocess

# Data processing imports
import warnings

# Plotting imports
import matplotlib
matplotlib.use('Agg')

from threading import Lock

import os
import openai
import sys

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
    return render_template('results.html', title='YouTube Summary')

@app.route('/set_wallpaper', methods=['POST'])
def set_wallpaper():
    try:
        image_path = request.form['image_path']
        # Use the appropriate command for your operating system
        if sys.platform.startswith('linux'):
            command = 'gsettings set org.gnome.desktop.background picture-uri file://{}'.format(image_path)
        elif sys.platform.startswith('win'):
            command = 'REG ADD \"HKCU\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d {} /f'.format(image_path)
            subprocess.run(command, shell=True)
            command = 'rundll32.exe user32.dll, UpdatePerUserSystemParameters'
        elif sys.platform.startswith('darwin'):
            command = 'osascript -e \'tell application "Finder" to set desktop picture to POSIX file "{}"\''.format(image_path)

        subprocess.run(command, shell=True)
        print('Wallpaper set successfully.')
    except subprocess.CalledProcessError:
        print('There was an error setting the wallpaper.')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
