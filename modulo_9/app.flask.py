from flask import Flask, jsonify

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

# Rota padrão - GET
@app.route('/',)

def obter_postagens():
  return jsonify(postagens)

app.run(port=7777, host='localhost', debug=True)

