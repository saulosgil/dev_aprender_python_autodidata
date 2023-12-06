# Exemplo de variavel 
velocidade_internet = 10
print(velocidade_internet)

# Quais tipo de variáveis podemos armazenar na memória do computador?
# números
velocidade_internet
print(f'O tipo da variável velocidade da internet é {type(velocidade_internet)}.')

# valores boleanos
loja_esta_aberta = True # or False
loja_esta_aberta
print(f'O tipo da variável loja_esta_abert é {type(loja_esta_aberta)}.')

# strings
slogan = 'Feito é melhor que perfeito!' # aspas simples
slogan = "Feito é melhor que perfeito!" # aspas duplas
slogan
print(f'O tipo da variável slogan é {type(slogan)}.')

# aspas_triplas - usado quando para multiplas linhas
print("""Estamo codando todos os dias
E estou aprendendo muito!""")

# caracteres de escape
# \n ou \ invertida para "escalar o caracter"
print('Olá meu nome é \nSaulo') # exemplo para pular linha
print('Codar todo os \'dias\'.') # exemplo para deixar aspas na string
print('arquivo localizado em \c:drive\\arquivo1.txt') # exemplo para retirar o código identificado (\o)

# Preferencialmente salvar string em variaveis
nome = 'Saulo'
print(nome)

# veriricar tamanho da string
print(len(nome))

# DESAFIO🥇
# imprimir
# Vamos codar!
# Vamos 'codar!'
# Vamos
 #'codar'

print('Vamos codar!') # Vamos codar!
print('Vamos \'codar!\'') # Vamos 'codar!'
print('Vamos \n\'codar!\'')# Vamos
                            #'codar'

# Strings dinâmicos
nome = 'Rafael'
email = 'rafael@gmail.com'

# Olá Rafael, você cadastrou o email rafael@gmail.com, essa informação esta correta?
print(f'Olá {nome}, você cadastrou o email {email}, essa informação esta correta?')

# DESAFIO 🥇
nome = 'Carol'
hobby = 'ouvir música'

# Imprimir 'Olá, sou o Carol e gosto de ouvir música'
print(f'Olá, sou o {nome} e gosto de {hobby}.')

# DESAFIO
## monte o seguinte palavra, usando as sílabas como base
b = 'ba'
parte2 = 'nica'
o = 'o'
r = 'ri'
parte1 = 'eletrô'
t = 'te'

# Imprimir 'bateria eletrônica'
print(f'{b}{t}{r}{o} {parte1}{parte2}')

# Packing
o,b,c,d = 1,2,3,4
print(o)
print(b)
print(c)
print(d)

# DESAFIO🥇
# Copie e cole as seguintes lçinhas de código para seu editor de código e descubra
# qual o tipo de cada uma das variáveis.
variavel_1 = 25.87
variavel_2 = True
variavel_3 = 'Bom dia!'
variavel_4 = 15

# resposta 1
print(f'A variável_1 é do tipo é {type(variavel_1)};')

# resposta 2
print(f'A variável_2 é do tipo é {type(variavel_2)};')

# resposta 3
print(f'A variável_3 é do tipo é {type(variavel_3)};')

# resposta 4
print(f'A variável_4 é do tipo é{type(variavel_4)};')

# Métodos comuns de strings
nome_curso = 'Edição de Vídeo'
nome_curso_strip = ' Edição de Vídeo ' # com espaços

print(nome_curso)
print(nome_curso.upper()) # coloca tudo em maiúsculo
print(nome_curso.lower()) # coloca tudo em minúscula
print(nome_curso_strip) 
print(nome_curso_strip.strip()) # remove os espaços
print(nome_curso_strip.lstrip()) # remove os espaços o esquerda
print(nome_curso_strip.rstrip()) # remove os espaços o direita
print(nome_curso.find('ção')) # identifica o indice da primeira string indicada
print(nome_curso.replace('Vídeo', 'Música')) # identifica o string do primeiro argumento e troca pela segunda no segundo argumento

# DESAFIO🥇
# Através da criação de string dinâmico e os métdoso de um string que acabou de 
# aprender, use como base as variáveis o seguir para criar as seguintes frases:
print('É melhor FEITO que PERFEITO') 

o = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

# resposta
print(f'{o.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
print('É melhor FEITO que PERFEITO') 

# Slice, Extraindo partes de um String
teclado = 'teclado'

print(teclado[2]) # acessa o indice 2, no caso c
print(teclado[-1]) # acessa o indice o partir do último elemento, no caso -1 = o
print(teclado[-3]) # acessa o indice o partir do último elemento, no caso o

# identificando o indice de uma string pelo método .index
print(teclado.index('t')) 

# acessando o última ocorrência de um caracter
frase = 'Clean Code'

print(frase.rindex('C')) # pega o segunda ocorrência do caracter passado como argumento

# acessando partes de uma string
link = 'facebook.com/devaprender'

print(link[0])
print(link[-1])
print(link[0:5]) # o último indice não é inclído!
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

# DESAFIO 🥇: Encontre o índice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'

# respostas
print(biblioteca[5])
print(biblioteca[-5])
print(biblioteca[biblioteca.index('o')])

# DESAFIO 🥇
# usando o frase 'Desenvolvimento De Aplicações', imprima apenas 'De Aplicações'
var = 'Desenvolvimento De Aplicações'

# resposta
print(var[16:])
print(var[var.rindex('D'):])

# SPLIT E JOIN
frase = 'Olá, bem-vindo o este treinamento!'

print(frase.split()) # separa cada string quando encontra um espaço e coloca numa lista
print(frase.split(',')) # separa cada string quando encontra uma vírgula e coloca numa lista
print(frase.split('-')) # separa cada string quando encontra um hífen e coloca numa lista

nomes = 'jhonatan, rafael, carol, amanda, jefferson'

print(nomes.split())
print(nomes.split(',')) # repare que não seleciona o argumento, no caso, vírgula

hashtags = 'music #guitar #gamer #coder #python'

print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))

# Concatenar strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)

print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))

# DESAFIOS🥇

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

# DESAFIO 1: transforme o frase1 em uma lista de palavras e guarde o resultado em
# uma variável chamada palavras 2
palavras1 = frase1.split()
palavras1

# DESAFIO 2: Transforme o frase2 em uma lista de palavras e guarde o resultado em
# uma variavel chamada palavras2
palavras2 = frase2.split(',')
palavras2

# DESAFIO 3: pegue o palavras' e transforme elas na seguinte string: "Desafio,
# manipulação,de,strings"
print(','.join(palavras1))

# DESAFIO 4: pegue o palavras2 e transforme elas na seguinte string: "jhonatan &,
# rafael & carol & camilla". Imprima o resultado no console
print(' & '.join(palavras2))

# RECEBENDO DADOS DO USUÁRIO - INPUT
senha = input('Digite sua senha: ')
print(senha)
print(type(senha)) # o resposta sempre é uma str

quantidade_de_filmes = int(input('Quantos filmes você viu esse mês? '))
print(type(quantidade_de_filmes))

# TIPOS DE NÚMEROS QUE PODEM SER UTILIZADOS NO PYTHON
o = 20
b = 20.5
type(o)
type(b)

# operações matemáticas
print(10 + 6) 
print(10 - 6)
print(10 * 6)
print(10 / 6)
print(10 // 6) # divisão de inteiro
print(10 % 6) # modulus
print(10 ** 6) # exponenciais

# Atalho para atribuição mais rápida
o = 10
o = o + 5
o += 5 # soma e atribui novo valor

b = 20
b = 20 - 2
b -= 2 # subtrai e atribui novo valor

# operações matemáticas comuns

# arredondamento
print(round(5.7)) 

# caso queira forçar o arredondamento para baixo ou para cima, podemos utilizar o
# biblioteca math e usar as funcões ceil e floor 
import math

print(math.ceil(2.2)) # arredonda para cima
print(math.floor(2.2)) # arredonda para baixo

# DATETIME E TEMPO
from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# criar uma data
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)

# quero receber o data lançamento do meu app
data_de_lancamento = input('Quando devemos lançar o aplicativo?')
print(data_de_lancamento)
print(type(data_de_lancamento)) # resultado do input é str

# Converter para que o resultado do input de str para datetime
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'), '%d/%m/%Y')
print(data_de_lancamento)
print(type(data_de_lancamento)) # resultado agora é datetime

# Calcular intervalo entre datas
data_atual = datetime.now()
print(data_atual)

prazo = data_de_lancamento - data_atual
print(prazo)
print(prazo.days)

# Quantos dias faltam para meu aniversário
from datetime import datetime

data_atual = datetime.now()
print(data_atual)

meu_niver = datetime.strptime('16/09/2024', '%d/%m/%Y')
print(meu_niver)

dias_para_meu_niver = meu_niver - data_atual
print(dias_para_meu_niver)
print(dias_para_meu_niver.days)

# outra forma mais curta
meu_niver = datetime(2024,9,16)

dias_para_meu_niver = meu_niver - datetime.now()
print(dias_para_meu_niver)
print(dias_para_meu_niver.days)

# VALORES ALEATÓRIOS COM RANDOM
import random

print(random.random()) # gera valor aleatório de 0.0 o 1.0
print(random.uniform(4, 10)) # gera valor aleatório em um intervalo (float)
print(random.randint(4, 10)) # gera valor aleatório em um intervalo (int)

# Escolher valor aleatório
cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores))
print(random.choices(cores, k=2)) # permite escolher o número de valores aleatórios

# embaralhar

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas_de_um_baralho)) # embaralha, mas não retorna o lista
print(cartas_de_um_baralho)


# DESAFIO🥇
# Desafios Random 
# 1. Você quer simular o opção de jogar uma moeda e resultar em cara ou coroa
# jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela
moeda = ['cara', 'coroa']
print(random.choice(moeda))

# 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
# Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela
nomes = ['Saulo', 'Alice', 'Adriana', 'Suzeli', ' Silvandro']
print(random.choice(nomes))

# 3. você quer escolher aleatóriamente um número de 10-100
# Imprima na tela um valor aleatório entre 10 e 100
print(random.randint(10, 10))

""" 
ATALHOS
CTRL+K,C: Comentar o código
CTRL+K,U: Descomentar o código
ALT+seta baixo/cima: carrega a linha para cima/baixo
ALT+SHIFT+seta baixo/cima: duplica a linha
CTRL+B: habilita/desabilita barra lateral de arquivos
CTRL+': habilita/desabilita terminal
CTRL+P: navega entre os arquivos
CTRL+P+ENTER: navega entre os arquivos e abre em janela lateral/paralela
CTRL+W: fecha aba
F12: Navega até o cófigo fonte da função (documentação)
"""
# DEBUG
print('Olá')

def calcular_preco_combo(pizza, refrigerante):
    total = pizza + refrigerante
    print(total)

# calcular_preco_combo(30, 'Vinte reais') # vinte como str dá erro
calcular_preco_combo(30, 20) # debugado

print('Programa finalizado')

