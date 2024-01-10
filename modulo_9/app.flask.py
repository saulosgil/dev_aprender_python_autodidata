from flask import Flask, jsonify, request

app = Flask(__name__)

postagens = [
  {
    'título': 'Minha História',
    'autor': 'Amanda Dias'
  },
  {
    'título': 'Novo Dispositivo Sony',
    'autor': 'Howard Stringer'
  },
  {
    'título': 'Lançamento do ano',
    'autor': 'Jeff Bezos'
  }
]

# Rota padrão - GET http://localhost:7777
@app.route('/')
def obter_postagens():
  return jsonify(postagens)

# Get com id - GET http://localhost:7777/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
  return jsonify(postagens[indice])

app.run(port=7777, host='localhost', debug=True)

