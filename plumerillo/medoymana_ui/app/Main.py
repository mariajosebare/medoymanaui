import os

import requests
from flask import Flask, render_template, request, flash, session

app = Flask(__name__)
app.secret_key = "w9z$C&F)"

"""UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER"""


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/contacto', methods=['GET'])
def contacto():
    return render_main('pages/contacto.html', title='Contacto')


@app.route('/perfil', methods=['GET'])
def perfilusuario():
    result = {
        'habilidades': session['habilidades']
    }
    return render_main(
        'pages/perfil-usuario.html',
        result=result,
        title='Perfil de usuario'
    )


@app.route('/chatusuario', methods=['GET'])
def chatUsuarios():
    return render_template('pages/chat-usuarios.html')


@app.route("/publicaciones/<int:id_habilidad>", methods=['GET'])
def publicacion(id_habilidad):
    # result = {
    #    'habilidades': Habilidades.seleccionar_todos(),
    #    'necesidades': Necesidades.seleccionar_por_usuario(id_habilidad)
    # }
    return render_template('pages/publicaciones.html', result=result)


@app.route("/matcheo/<int:id_necesidad>", methods=['GET'])
def matcheo(id_necesidad):
    # necesidad = Necesidades.seleccionar_por_id(id_necesidad)
    # result = {
    #    'necesidades': Necesidades.seleccionar_match(necesidad['ID_usuario'], necesidad['ID_habilidad']),
    #    'publicacion': necesidad
    # }
    return render_template('pages/matcheo.html', result=result)


@app.route("/login", methods=['GET', 'POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    response = requests.post("http://localhost:5000/login", data).json()
    if 'error' in response:
        flash(response['error'])
    else:
        session['usuario'] = response['usuario']
        session['habilidades'] = response['habilidades']
        return perfilusuario()


def render_main(template_name_or_list, result=None, title=None):
    return render_template(**locals(), usuario=session.get('usuario'))


if __name__ == '__main__':
    app.run(host="localhost", port=5001, debug=True)
