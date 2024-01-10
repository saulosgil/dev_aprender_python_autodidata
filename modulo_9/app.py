# Como usar os 4 principais comandos (verbos) de uma API

'''
Site usado para consultar uma API:

https://jsonplaceholder.typicode.com/
'''
import requests
from pprint import pprint # exibe o resultado de uma API de forma mais legivel 

# GET - obter todos os recursos
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
pprint(resultado_get) # exibe o a resposta 200 (Response [200]) que indica Sucesso na requisição deu certo   
pprint(resultado_get.json()) # exibe o resultado em um formato mais legível

# GET com ID
resultado_get_id = requests.get('https://jsonplaceholder.typicode.com/todos/2') # insere a tarefa que quer obter
pprint(resultado_get_id) # exibe a resposta 200 (Response [200]) que indica Sucesso na requisição deu certo   
pprint(resultado_get_id.json()) # exibe o resultado em um formato mais legível

# POST - criar um novo recurso
'''
Criar uma nova tarefa no mesmo formato (JSON). Para isso, basta copiar o output do get realizado
anteriormente.

o output é:

{'completed': False,
 'id': 2,
 'title': 'quis ut nam facilis et officia qui',
 'userId': 1}

 Usar como referencia para criar uma outra tarefa
'''
nova_tarefa = {'completed': False,'title': 'Lavar o carro', 'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)
pprint(resultado_post) # exibe a resposta 201 (Response [201]) que indica Sucesso na requisição deu certo   
pprint(resultado_post.json()) # exibe o resultado em um formato mais legível

'''
Repare que a tarefa foi alterada conforme solicitado:
{'completed': 'False', 'id': 201, 'title': 'Lavar o carro', 'userId': '1'}
'''

# PUT - altera um recurso existente
tarefa_alterada = {'completed': False,'title': 'Lavar o moto', 'userId': 1}

resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
pprint(resultado_put) # exibe a resposta 200 (Response [20]) que indica Sucesso na requisição deu certo   
pprint(resultado_put.json()) # exibe o resultado em um formato mais legível

'''
Repare que a tarefa foi alterada conforme solicitado:
{'completed': 'False', 'id': 2, 'title': 'Lavar o moto', 'userId': '1'}'''

# Delete - remover algum recurso
reseulado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(reseulado_delete) # exibe a resposta 200 (Response [20]) que indica Sucesso na requisição deu certo   
pprint(reseulado_delete.json()) # exibe o resultado em um formato mais legível

'''
repare que a tarefa passada, agora retorna um dicionário vazio.
{}
'''



