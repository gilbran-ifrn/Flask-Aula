from flask import Flask
from flask import render_template
from flask import request

import mysql.connector

app = Flask(__name__)

def conexaoBD():
    cnx = mysql.connector.connect(user='root',
                                password='senhabd',
                                host='127.0.0.1',
                                database='babel')
    return cnx

@app.route('/')
def inicial():
    conexao = conexaoBD()
    cursor = conexao.cursor(dictionary=True)

    sql = ("SELECT idioma, mensagem FROM texto")

    cursor.execute(sql)

    mens = cursor.fetchall()

    return render_template('inicial.html', todoDicionario=mens)

@app.route('/<idioma>')
def olaMundo(idioma):
    conexao = conexaoBD()
    cursor = conexao.cursor(dictionary=True)

    sql = ("SELECT mensagem FROM texto "
           "WHERE idioma = %s")
    
    tupla = (idioma,)

    cursor.execute(sql, tupla)

    mens = cursor.fetchone()

    if (cursor.rowcount > 0):
        cursor.close()
        conexao.close()
        return render_template('mensagens.html', mensagem=mens['mensagem'])
    else:
        cursor.close()
        conexao.close()
        return render_template('mensagens.html', mensagem='Não tenho conhecimento')
        
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    i = request.form['idi']
    m = request.form['mens']

    conexao = conexaoBD()
    cursor = conexao.cursor()

    sql = ("INSERT INTO texto "
           "(idioma, mensagem) "
           "VALUES (%s, %s)")

    tupla = (i, m)

    cursor.execute(sql, tupla)
    conexao.commit()

    cursor.close()
    conexao.close()

    return render_template('resposta.html')

    
