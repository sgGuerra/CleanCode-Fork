from flask import Flask
from flask import render_template, request , url_for, jsonify
import sys 
sys.path.append("src")

from controller.saving_controller import *

app = Flask(__name__)

@app.route('/')
def select():
    seleccionando = select_savings("2")
    return render_template("index.html", seleccionando = seleccionando)

if __name__ == '__main__':
    app.run(debug=True)