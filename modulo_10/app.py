# Processando itens de uma lista com MAP

# Usando Loops
numeros = []

for i in range(5):
  numeros.append(i)

print(numeros)

# Usando a função MAP - aplica um fct a um vetor/array
nomes = ['larissa', 'Rafael', 'Marcus', 'John']

# Fct que será aplicada
def aprovar_pessoa(nome):
  return nome + ' APROVADO'

# Aplicando a fct no array com MAP
print(map(aprovar_pessoa, nomes)) # precisa converter em lista
print(list(map(aprovar_pessoa, nomes)))

# List Compreheension
'''
Uma List Comprehension em Python é uma forma concisa e poderosa de criar listas.
Ela permite que você crie novas listas a partir de iteráveis (como listas, tuplas,
conjuntos, etc.) de uma maneira mais compacta e legível.

A sintaxe básica de uma List Comprehension é a seguinte:

**nova_lista = [expressão for item in iterável if condição]**

expressão: É o valor que será armazenado na nova lista;

item: É a variável que representa cada elemento do iterável;

iterável: É a coleção de elementos que está sendo percorrida (por exemplo, uma lista,
tupla, conjunto, ou até mesmo uma string).

if condição (opcional): É uma condição opcional que filtra os elementos do iterável com
base em uma expressão booleana.
'''
quadrados = [x ** 2 for x in range(1, 6)]
print(quadrados)

# ex. 2
nomes = ['larissa', 'Rafael', 'Marcus', 'John']
print([nome + ' Aprovado' for nome in nomes])

# ex. 3 - Criar matriz
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
from pprint import pprint
pprint([[i for i in range(1,6)] for x in range(6)])

# Usando condicionais na list compreheension (pegar fct aprovar pessoa)
nomes = ['larissa', 'Rafael', 'Marcus', 'John']
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])

# Ex. numérico
print([i for i in range(20) if i not in (1,2,15,19)])

# Ex. numérico - usando uma fct
def eh_numero_par(numero):
  valor = numero % 2
  if valor == 0:
    return True
  else:
    return False

print([i for i in range(20) if eh_numero_par(i)])

# Desafio 1
from pprint import pprint

# Usando a lista compreheension, crie a seguinte lista:
[2, 4, 6, 8, 10]

# Resposta
pprint([i * 2 for i in range(1,6)])

# Desafio 2
# Use a seguinte lista como base:
cores = ['vermelho','azul','verde','amarelo','rosa','preto']

# Para criar a lista a seguir:
['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rose','6 - preto']

# Resposta
pprint([str(cores.index(i)+1) + ' - ' + i for i in cores])

# Desafio 3 
# Usando a lista a seguir como base:
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','marcia','cris']
'''
Concatene(adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais
somente nos casos onde seu nome esteja na lista 'pagamento_realizado'. O resultado final
deve ser como a lista a seguir:
'''
['joel PAGO','jessica PAGO','maria PAGO','cris PAGO','Larissa','rafael','marcus','john']

print([i + ' Pago' if i in pagamento_realizado else i + ' Devendo' for i in participantes])

# Dictionary Compreheension
'''
Uma Dictionary Comprehension em Python é uma maneira concisa e eficiente de criar dicionários.
Assim como as List Comprehensions, as Dictionary Comprehensions permitem criar dicionários
em uma única linha de código de forma legível e eficiente.

A sintaxe básica de uma Dictionary Comprehension é semelhante à List Comprehension, mas em
vez de criar uma lista, você cria um dicionário.

A sintaxe básica é:

novo_dicionario = {chave: valor for item in iterável}

onde:
chave: É a chave do dicionário; 
valor: É o valor associado à chave; 
item: É a variável que representa cada elemento do iterável; 
iterável: É a coleção de elementos que está sendo percorrida (por exemplo, uma lista, tupla,
conjunto, ou até mesmo uma string)
'''
from random import randint
from pprint import pprint

pprint({i: i for i in range(20)})

# ex1. Popular dicionarios
produtos = ['produto1', 'produto2', 'produto3', 'produto4', 'produto5']

pprint({produto: 1 for produto in produtos})

# Gerar matriz de valores teste
pprint({produto: [0 for i in range(5)] for produto in produtos})
pprint({produto: [i*2 for i in range(5)] for produto in produtos})

pprint({produto: [randint(1000,15000) for i in range(5)] for produto in produtos}) # com valores aleatórios


# Desafios 🥇
# Desafio 1 

# Usando a lista seguir como base:

'''
sorteios = ['sorteio1','sorteio2','sorteio3']

participantes = ['joel','jessica', 'maria','cris','Larissa', 'rafael', 'marcus', 'john']
'''

# crie a seguir, selecionando o ganhador aleatóriamente um nomes da lista de participantes. A ideia é simular quem irá ganhar cada sorteio, sua lista deve gerar a seguinte estrutura(porém o nome pode vir a ser diferente, já que estamos selecionando os nomes aleatóriamente)
'''
{

    sorteio1: 'cris',

    sorteio2: 'rafael',

    sorteio3: 'marcus',

}
'''
import random
from pprint import pprint

sorteios = ['sorteio1','sorteio2','sorteio3']
participantes = ['joel','jessica', 'maria','cris','Larissa', 'rafael', 'marcus', 'john']

pprint({sorteio: random.choice(participantes) for sorteio in sorteios})

# Desafio 2
'''
Precisamos de dados de testes para criar contas temporárias, no momento precisamos de gerar 5
valores de 1 a 100, e esses valores precisam Precisamos gerar 5 valores de 1 a 100 aleatóriamente.

E estes valores precisam ser gerados para cada grupo na lista abaixo grupos 
'''
grupos = ['grupo 1', 'grupo 2', 'grupo 3']

'''O resultado esperado é o dicionário com a estrutura a seguir(os valores entre contindos dentro da lista estarão diferentes, uma vez que os valores abaixo foram geradores aleatóriamente)

{

 'grupo 1': [93, 97, 63, 36, 34],

 'grupo 2': [81, 24, 22, 46, 52],

 'grupo 3': [5, 35, 6, 86, 37]

}
'''
import random
from pprint import pprint

grupos = ['grupo 1', 'grupo 2', 'grupo 3']
pprint({grupo: [randint(1,101) for i in range(5)] for grupo in grupos})








