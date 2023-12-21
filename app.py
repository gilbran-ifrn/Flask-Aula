from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

idiomas = {
    'portugues': 'Olá, Mundo!',
    'ingles': 'Hello, World!',
    'frances' : 'Salut, Monde!'
}

@app.route('/')
def inicial():
    return render_template('inicial.html', todoDicionario=idiomas)

@app.route('/<idioma>')
def olaMundo(idioma):
    try:
        return render_template('mensagens.html', mensagem=idiomas[idioma])
    except:
        return render_template('mensagens.html', mensagem='Não tenho conhecimento!')
    
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    i = request.form['idi']
    m = request.form['mens']

    idiomas[i] = m

    return render_template('resposta.html', idio=idiomas)

    
