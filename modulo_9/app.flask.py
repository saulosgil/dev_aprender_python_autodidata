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

# Obter postagem por id - GET http://localhost:7777/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
  return jsonify(postagens[indice])

# criar uma nova postagem - POST http://localhost:7777/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
  postagem = request.get_json()
  postagens.append(postagem)

  return jsonify(postagem, 200)

'''
entrar no Postman - fazer a requisição no http://localhost:7777/postagem com o
método POST:
  1 - ir na aba Body;
  2 - ir na aba secundária raw e colocar JSON;
  3 - passar as informações (formato JSON);
{
    "autor": "Hermar Li",
    "título": "Novo album da banda"
}
  4 - Apertar Send;
  5 - verificar STATUS para ver se foi inserido corretamente
'''

# Alterar uma postagem existente - PUT
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
  postagem_alterada = request.get_json()
  postagens[indice].update(postagem_alterada)

  return jsonify(postagens[indice], 200)

'''
entrar no Postman - fazer a requisição no http://localhost:7777/postagem/1 com o
método PUT:
  1 - ir na aba Body;
  2 - fazer a alteração desejada
{
    "título": "Novo album da banda 2023"
}
  4 - Apertar Send;
  5 - verificar STATUS para ver se foi inserido corretamente
'''

# excluir uma postagem - DELETE http://localhost:7777/postagem/1
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
  try:
    if postagens[indice] is not None:
      del postagens[indice]
      return jsonify(f'Foi excluído a postagem {postagens[indice]}', 200)
  except:
    return jsonify(f'Não foi possível encontrar a postagem para exclusão', 404)

# roda o programa
app.run(port=7777, host='localhost', debug=True)

