from flask import Flask
from flask import render_template, request , url_for, jsonify, redirect
import sys 
sys.path.append("src")

from controller.saving_controller import *

app = Flask(__name__)

@app.route('/')
def seleccionar():
    seleccionados = select_all_savings()
    return render_template("index.html", seleccionando = seleccionados)

@app.route('/buscar', methods=['GET'])
def buscar():
    buscar = request.args.get('buscar', '')
    if buscar == '':
        resultados = select_all_savings()
        return render_template("index.html", seleccionando = resultados)
    else:
        resultados = []
    try:
        id_buscar = int(buscar)
        resultados = select_savings(id_buscar)
    except ValueError:
        try:
            monto_buscar = float(buscar)
            resultados = select_saving_monto(monto_buscar)
        except ValueError:
            resultados = []
    return render_template("index.html", seleccionando = resultados)

@app.route('/agregar', methods=['POST'])
def agregar():
    monto = request.form['monto']
    interes = request.form['interes']
    periodo = request.form['periodo']
    saving = Saving(monto, interes, periodo)
    insert_saving(saving)
    return redirect('/')

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_ahorro(id):
    delete_saving(id)
    return redirect('/')

@app.route('/modificar/<int:id>', methods=['POST'])
def modificar_ahorro(id):
    monto = request.form['monto']
    interes = request.form['interes']
    periodo = request.form['periodo']
    saving = Saving(monto, interes, periodo, id=id)  # Ajusta según tu modelo
    update_saving(saving)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)