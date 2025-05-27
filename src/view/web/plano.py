import sys 
sys.path.append("src")

from flask import Blueprint, render_template, request, redirect
from werkzeug.exceptions import BadRequestKeyError
from controller.saving_controller import *

blueprint = Blueprint("vista_usuario", __name__, "templates")

# Define las rutas de la aplicación web
# @blueprint.route('/')
# def seleccionar():
#     seleccionados = select_all_savings()
#     return render_template("index.html", seleccionando = seleccionados)

@blueprint.route('/', methods=['GET', 'POST'])
def seleccionar():
    if request.method == 'POST':
        create_savings_table()  # Llama a la función que crea la base de datos
        return redirect('/')
    seleccionados = select_all_savings()
    db_existe = verificar_si_db_existe()  # Implementa esta función en tu controller
    return render_template("index.html", seleccionando=seleccionados, db_existe=db_existe)

@blueprint.route('/buscar', methods=['GET'])
def buscar():
    buscar = request.args.get('buscar', '')
    db_existe = verificar_si_db_existe()
    if buscar == '':
        resultados = select_all_savings()
        return render_template("index.html", seleccionando = resultados, db_existe= db_existe)
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
    return render_template("index.html", seleccionando = resultados, db_existe=db_existe)

@blueprint.route('/agregar', methods=['POST'])
def agregar():
    monto = request.form['monto']
    interes = float(request.form['interes'])
    periodo = int(request.form['periodo'])

    if periodo < 1 or periodo > 12:
        return "El período debe estar entre 1 y 12 meses.", 400
    if interes < 0 or interes > 10:
        return "El interés debe estar entre 0% y 10%.", 400

    saving = Saving(monto, interes, periodo)
    insert_saving(saving)
    return redirect('/')

@blueprint.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_ahorro(id):
    delete_saving(id)
    return redirect('/')

@blueprint.route('/accion/<int:id>', methods=['POST'])
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

# Mostrar el formulario de modificación (GET)
@blueprint.route('/modificar/<int:id>', methods=['GET'])
def mostrar_formulario_modificar(id):
    saving = select_savings(id)
    if not saving:
        return redirect('/')
    return render_template('modificar.html', saving=saving, id=id)

# Procesar la modificación (POST)
@blueprint.route('/modificar/<int:id>', methods=['POST'])
def modificar_ahorro(id):
    monto = request.form['monto']
    interes = request.form['interes']
    periodo = request.form['periodo']
    saving = Saving(monto, interes, periodo)
    update_saving(id, saving)
    return redirect('/')


@blueprint.errorhandler(Exception)
def manejar_error(err):
    return f'¡Opss! ocurrio un error: {err}'

@blueprint.errorhandler(BadRequestKeyError)
def manejar_error(err):
    return f'¡Opss! ocurrio un error: {err}'

@blueprint.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error.html'), 404

@blueprint.errorhandler(405)
def metodo_no_permitido(error):
    return render_template('error.html'), 405

