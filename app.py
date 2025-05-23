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

@app.route('/accion/<int:id>', methods=['POST'])
def accion_general(id):
    accion = request.form.get('accion')

    if accion == 'eliminar':
        delete_saving(id)
        return redirect('/')

    elif accion == 'modificar':
        saving = select_savings(id)
        if not saving:
            return redirect('/')
        return render_template("modificar.html", saving=saving, id=id)

    return "Acción no reconocida", 400

@app.route('/modificar/<int:id>', methods=['POST'])
def modificar_ahorro(id):
    monto = request.form['monto']
    interes = request.form['interes']
    periodo = request.form['periodo']

    saving = Saving(monto, interes, periodo)
    update_saving(id, saving)
    return redirect('/')


@app.route('/modificar/<int:id>', methods=['POST'])
def mostrar_formulario_modificar(id):
    saving = modificar_ahorro(id)  # Función que devuelve un objeto Saving o lista con datos
    if not saving:
        return redirect('/')  # O mostrar error
    return render_template('modificar.html', saving=saving, id=id)


if __name__ == '__main__':
    app.run()