# Módulo e função
from flask import Flask, jsonify, request

# flask object implements a WSGI application
app = Flask(__name__)

# Lista das músicas 
cancoes = [
    {
        'cancao': 'cancao 1',
        'estilo': 'hip-hop'
    },
    {
        'cancao': 'cancao 2',
        'estilo': 'rock'
    },
    {
        'cancao': 'cancao 3',
        'estilo': 'pop'
    }
]

# Rota padrão - GET http://localhost:5000/cancoes
@app.route('/cancoes', methods=['GET'])
def obter_todas_cancoes():
    return jsonify(cancoes)

# Obter musica por id - GET http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:cancao_id>', methods=['GET'])
def obter_cancao_por_id(cancao_id):
    return jsonify(cancoes[cancao_id])

# criar uma nova musica - POST http://localhost:5000/cancoes
@app.route('/cancoes', methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(f'A canção: {cancao} foi adiciona com sucesso', 200)

'''
Para teste, adicionei o cancao 4:
{
    "cancao": "cancao 4",
    "estilo": "funk"
}
'''

# alterar uma musica  existente - PUP http://localhost:5000/cancoes
@app.route('/cancoes/<int:cancao_id>', methods=['PUT'])
def atualizar_cancao(cancao_id):
    cancao_alterada = request.get_json()
    cancoes[cancao_id].update(cancao_alterada)
    return jsonify(cancoes[cancao_id], 200)

'''
Para teste, alterei o estilo da cancao 4 - funk para classica:
{
    "estilo": "classica"
}
'''

# deletar uma musica existente pelo id - PUP http://localhost:5000/cancoes/3
@app.route('/cancoes/<int:cancao_id>', methods=['DELETE'])
def excluir_cancao(cancao_id):
    try:
        del cancoes[cancao_id]
        return jsonify({'mensagem': 'A canção foi excluída com sucesso!'})
    except:
        return jsonify('Não foi encontrado uma canção com este id', 404)

'''
Para teste, removi a cancao 4
'''

# roda o programa
app.run(port=5000, host='localhost', debug=True)