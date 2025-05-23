from flask import Blueprint, render_templatem, request

from werkzeug.exceptions import BadRequestKeyError


blueprint = Blueprint('vista', __name__, "templates")


from flask import render_template, request, redirect
import sys 
sys.path.append("src")

from controller.saving_controller import *



@blueprint.route('/')
def seleccionar():
    seleccionados = select_all_savings()
    return render_template("index.html", seleccionando = seleccionados)

@blueprint.route('/buscar', methods=['GET'])
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

@blueprint.route('/agregar', methods=['POST'])
def agregar():
    monto = request.form['monto']
    interes = request.form['interes']
    periodo = request.form['periodo']
    saving = Saving(monto, interes, periodo)
    insert_saving(saving)
    return redirect('/')

@blueprint.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_ahorro(id):
    delete_saving(id)
    return redirect('/')

@blueprint.route('/modificar/<int:id>', methods=['POST'])
def modificar_ahorro(id):
    monto = request.form['monto']
    interes = request.form['interes']
    periodo = request.form['periodo']
    saving = Saving(monto, interes, periodo, id=id)  # Asegúrate de que el modelo permita pasar el ID
    update_saving(saving)
    return redirect('/')


@blueprint.errorhandler(Exception)
def manejar_error(err):
    return f'¡Opss! ocurrio un error: {err}'


@blueprint.errorhandler(BadRequestKeyError)
def manejar_error(err):
    return f'¡Opss! ocurrio un error: {err}'
