from flask import Flask, render_template, request, url_for, redirect
import joblib
import pandas as pd

app=Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
    prediction=""
    if request.method=='POST':
        age=int(request.form['age'])
        weight=int(request.form['weight'])

        clf = joblib.load("regr.pkl")
        x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
        prediction = clf.predict(x)[0]

    request.form=request.form.to_dict()
    request.form['age']=""
    request.form['weight']=""    
    return render_template('index.html', prediction=prediction, form=request.form)