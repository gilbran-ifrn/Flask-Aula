from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicial():
    return '<h1>Olá, Mundo!</h1>'

@app.route('/<idioma>')
def olaMundo(idioma):
    if idioma == 'portugues':
        mensagem = 'Olá, Mundo!'
    elif idioma == 'ingles':
        mensagem = 'Hello, World!'
    elif idioma == 'frances':
        mensagem = 'Salut, Monde!'
    else:
        mensagem = 'Não tenho conhecimento!'

    return f'<h1>{mensagem}</h1>'
