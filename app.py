from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

app = Flask(__name__)

bp = Blueprint('app', __name__)

nome = None
premio = None


@bp.route('/', methods=('GET', 'POST'))
def index():
    global premio, nome

    if request.method == 'POST':
        nome = request.form['nome']

        escolha_usuario = request.form['escolha']

        if escolha_usuario == "futurista":
            premio = "um Sabre de Luz"
        elif escolha_usuario == "medieval":
            premio = "uma Espada"
    else:
        nome = None
        premio = None

    return render_template('index.html', nome=nome, premio=premio)


app.register_blueprint(bp)
