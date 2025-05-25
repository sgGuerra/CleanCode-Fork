from flask import Flask
from flask import render_template
import sys 
sys.path.append("src")

from controller.saving_controller import *
from view.web import plano

app = Flask(__name__)

app.register_blueprint(plano.blueprint)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error.html', error_code=404, mensaje="¡Ups! Página no encontrada"), 404

@app.errorhandler(405)
def metodo_no_permitido(error):
    return render_template('error.html', error_code=405, mensaje="Método no permitido"), 405


if __name__ == '__main__':
    app.run(debug=True)