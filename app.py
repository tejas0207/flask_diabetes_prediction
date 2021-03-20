import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request


app = Flask("diabetisapp")

model = load_model('dia_model.h5', compile = False)

@app.route("/home")
def myhome():
    return render_template("index.html")

@app.route("/form")
def myform():
    return render_template("form.html")


@app.route("/result", methods=[ "GET" ] )
def result():
    x1 = request.args.get("z1")
    x2 = request.args.get("z2")
    x3 = request.args.get("z3")
    x4 = request.args.get("z4")
    x5 = request.args.get("z5")
    x6 = request.args.get("z6")
    x7 = request.args.get("z7")
    x8 = request.args.get("z8")
    output = model.predict([[ int(x1), int(x2), int(x3), int(x4), int(x5), float(x6), float(x7), int(x8) ]])
    final = (round(output[0][0]))
    if final == 1:
        return render_template("notsafe.html")
    else:
        return render_template("safe.html")
    return 
app.run()