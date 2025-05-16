# Ahorro Programado
# ¿Quién hizo esto?
Juan Esteban Marín Villegas
Tomás Mercado Ramos

# ¿Quien hizo la pagina web?
- Emanuel García
- Luis Carlos Guerra	

# ¿Quien hizo la interfaz gráfica?

* Juan José Becerra Bedoya
* Simon Correa Bravo

# ¿Qué es y para qué es?
El proposito de este proyecto es ayudarle a las persona a calcular de una manera más fácil y práctica el monto que van ahorrar con el ahorro programado

# ¿Cómo lo hago funcionar?
Prerrequisitos: 

Antes de correr el proyecto debes tener el conocimiento de la couta que se va dar mensual, el interés que se va aplicar y el numero de cuotas que se darán.

Ejecución:
Ubicados en la carpeta raiz del proyecto, ejecute:

py src\view\console.py


Ejecucion de interfaz grafica: 

python3 -m src.view.kivy_ahorro_programado

donde se corre como modulo para que funcione de manera correcta sus importaciones

# ¿Cómo está hecho?
La organización de los módulos es la siguiente:

En la carpeta src tenemos otras sub carpetas que son controller, model y view. Model contiene dos archivos, el obligatorio que es __init__.py y app.py que es donde está toda la lógica del proyecto. Controller solo contiene el archivo obligatorio __init__.py. Y view tiene un archivo que se llama console.py que contiene todo el código para tener interacción con el usuario por medio de la consola.

En la carpeta tests hay dos archivos casos de pruebas.xlsx y Tests.py. Casos de pruebas.xlsx es un excel con todos los casos de pruebs que nos fueron solicitados. Y Tests.py tiene todas las pruebas unitarias con sabe en esos casos de prueba.

# Estructura sugerida
Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
Carpeta tests: Pruebas Unitarias

# Uso
Para ejecutar las pruebas unitarias, desde la carpeta raiz, use el comando

py tests\Tests.py 

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

import sys sys.path.append("src")
