import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/scan1.html')
def scan1():
    return render_template('scan1.html')
@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')
@app.route('/se.html')
def se():
    return render_template('se.html')
@app.route('/chatnav.html')
def chatnav():
    return render_template('chatnav.html')
@app.route('/sam.html')
def sam():
    return render_template('sam.html')
@app.route('/Mymap1.html')
def Mymap1():
    return render_template('Mymap1.html')
@app.route('/graph.html')
def graph():
    return render_template('graph.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)


    return render_template('scan1.html', prediction_text='Your Risk Level Percentage {} %'.format(output))






if __name__ == "__main__":
    app.run(debug=True)