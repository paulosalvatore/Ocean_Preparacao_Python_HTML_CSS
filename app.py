from flask import (
    Blueprint, render_template, request
)
from flask import Flask

app = Flask(__name__)

bp = Blueprint('app', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    nome = None
    premio = None
    premio_imagem = None

    if request.method == 'POST':
        nome = request.form['nome']

        escolha_usuario = request.form['escolha']

        if escolha_usuario == "bulbassauro":
            premio = "Bulbassauro"
            # premio_imagem = "https://i.pinimg.com/originals/f5/72/7b/f5727b17d6e3cb84596deb8f96cbe071.gif"
            premio_imagem = "https://media3.giphy.com/media/11bZCpoCBpf3ck/giphy.gif"
        elif escolha_usuario == "charmander":
            premio = "Charmander"
            # premio_imagem = "https://media.indiedb.com/images/members/5/4384/4383197/profile/Knight.gif"
            premio_imagem = "https://i.pinimg.com/originals/37/08/62/370862bbff7f3d3345a3d0e9b45a38c3.gif"
        elif escolha_usuario == "squirtle":
            premio = "Squirtle"
            premio_imagem = "https://poketouch.files.wordpress.com/2017/06/squirtle_squad_leader_puts_sunglasses_on_in_the_pokemon_anime.gif"

    return render_template('index.html', nome=nome, premio=premio, premio_imagem=premio_imagem)


app.register_blueprint(bp)
