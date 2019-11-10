from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

"""
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


#@app.route('/api/', methods=['POST'])
@app.route("/")
def makecalc():
    data = [[1, 1, 70, 1, 1, 100.25]]
    #data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run()
    """