from flask import Flask
import flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/calculadora")
db = mongodb_client.db


@app.route("/")
def home():
    return "<h1>AH, LÁ UM OTÁRIO!</h1>"


@app.route('/adicao/<int:n1>/<int:n2>/')
def adicao(n1, n2):
    resultado = n1 + n2

    operacao = {
        "operacao" : "adicao",
        "numero1" : n1,
        "numero2" : n2,
        "resultado" : resultado
    }

    db.operacoes.insert_one(operacao)

    return "{:.1f}".format(resultado)


@app.route('/subtracao/<int:n1>/<int:n2>/')
def subtracao(n1, n2):
    resultado = n1 - n2

    operacao = {
        "operacao" : "subtracao",
        "numero1" : n1,
        "numero2" : n2,
        "resultado" : resultado
    }

    db.operacoes.insert_one(operacao)

    return "{:.1f}".format(resultado)


@app.route('/multiplicacao/<int:n1>/<int:n2>/')
def multiplicao(n1, n2):
    resultado= n1 * n2

    operacao = {
        "operacao" : "multiplicacao",
        "numero1" : n1,
        "numero2" : n2,
        "resultado" : resultado
    }

    db.operacoes.insert_one(operacao)

    return "{:.1f}".format(resultado)


@app.route('/divisao/<int:n1>/<int:n2>/')
def divisao(n1, n2):
    resultado = n1 / n2

    operacao = {
        "operacao" : "divisao",
        "numero1" : n1,
        "numero2" : n2,
        "resultado" : resultado
    }

    db.operacoes.insert_one(operacao)
    
    return "{:.1f}".format(resultado)
    

@app.route('/historico/')
def historico():

    operacoes = db.operacoes.find()

    operacoesDTO = [

        {
        'operacao' : operacao['operacao'], 
        'numero1' : operacao['numero1'], 
        'numero2' : operacao['numero2'],
        'resultado' : operacao['resultado']
        } 

        for operacao in operacoes
        ]

    return flask.jsonify(operacoesDTO)

if __name__ == '__main__':
    app.run(debug=True, port="5000")    