#Flask imports
from flask import Flask, render_template, send_file, make_response, url_for, Response
from flask_socketio import SocketIO

# Data processing imports
import os
import io
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter('ignore')
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import statsmodels.api as sm
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR

# Tensorflow imports
import tensorflow as tf
from tensorflow import keras, optimizers
from keras import backend, layers, metrics, Input
from keras.layers import Bidirectional, Dense, Dropout, LSTM, RNN 

# Plotting imports
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Other imports
from datetime import date, datetime, timedelta
from threading import Lock
import math
# from scraper import *

app = Flask(__name__)

sio = SocketIO(app)

thread = None
thread_lock = Lock()

@app.route('/')
@app.route('/results', methods=("POST", "GET"))
def index():
    global thread
    return render_template('results.html', title='New App')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)
