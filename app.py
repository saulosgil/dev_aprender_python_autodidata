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

# OPERADORES LÓGICOS 
# Pq queremos comparar ?
idade = 15

print(idade > 17)
print(idade < 17)
print(idade <= 17)
print(idade >= 17)
print(idade == 17)
print(idade != 17)

# Comparações entre outros tipo
print(True == False)
print('Rafael' == 'rafael')
print('b' > 'a')
print(5 == '5')

# Vamos pensar por exemplo no seguinte:
idade = 21
possui_convite = False
filho_do_dono = True

print((idade >= 21) and (possui_convite == True)) # and - se uma condição for false, ele retorna false
print((idade >= 21) or (possui_convite == True)) # or - se uma condição for true, ele retorna true

# maior de 21 anos E possui_convite OU seja filho do dono
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

# Example
maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

# você só pode trabalhar aqui se for maior de idade E possuir carteira de trabalho
print(maior_de_idade == True and possui_carteira_de_trabalho == False)
print(maior_de_idade and possui_carteira_de_trabalho)

# Queremos contratar pessoas que ainda não possuem um veículo próprio, mas já possuem 
# carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)

# Desafio 🥇

'''
Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.
'''
possui_passaporte = False
passagem_comprada = False
menor_de_idade = False


# E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela.
# Tente fazer cada condição e depois veja a solução no final deste aula.

# Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não for 
# menor de idade
print((possui_passaporte and passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for
#  menor de idade
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não 
# for menor de idade
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e 
# for menor de idade
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)

# OPERADORES DE IGUALDADE
a = 'Python'
b = 'Python'

print(a == b) # == compara o valor
print(a is b) # is compara a identidade

# Conversão de tipos de dados
idade = input('Qual é a sua idade?')
print(int(idade) > 18)

# Outra forma
idade = int(input('Qual é a sua idade?'))
print(idade > 18)

# Receber valores decimais
altura_da_parede = input('Qual a altura da parede?')
print(float(altura_da_parede) > 2.10)

# Outra forma:
altura_da_parede = float(input('Qual a altura da parede?'))
print(altura_da_parede > 2.10)

'''
Outras formas:
int()
str()
float()
list()
tuple()
list()
'''

# IF AND ELSE
trabalho_terminado = False

if trabalho_terminado == True:
    print('Bora dar uma saida!')
else: print('Não posso sair agora!')

# Exemplo 1
numero_atrasos = 2

if numero_atrasos >= 3:
    print('Vá para a diretoria')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta')
else:
    print('Pode entrar')

'''
A velocidade máxima para essa rua é 50km
    * cruzou entre 50 a 60km, levou multa de 2 pontos
    * cruzou entre 61 a 75km, levou multa de 3 pontos
    * cruzou acima de 75km, levou multa de 7 pontos
'''
velocidade = 100

if velocidade <= 50:
    print('Não foi multado')
elif velocidade >= 50 and velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 2 pontos')
else:
    print('Levou multa de 7 pontos')

# Chaining
if velocidade <= 50:
    print('Não foi multado')
# elif velocidade >= 50 and velocidade <= 60:
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
# elif velocidade >= 61 and velocidade <= 75:
elif 61 >= velocidade <=75:
    print('Levou multa de 2 pontos')
else:
    print('Levou multa de 7 pontos')

# Desafio 🥇

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do 
# corte de cabelos grandes que irá seguir as seguinte regras

'''
Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00

Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00

Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00

Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário
'''
tamanho_cabelo = 100

if tamanho_cabelo <= 20:
    print('O valor é R$50,00')
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print('O valor é R$70,00')
elif tamanho_cabelo >= 31 and tamanho_cabelo <= 50:
    print('O valor é R$100,00')
else:
    print('Favor consultar a recepção')

# Chaining
if tamanho_cabelo <= 20:
    print('O valor é R$50,00')
elif 21 <= tamanho_cabelo <= 30:
    print('O valor é R$70,00')
elif 31 <= tamanho_cabelo <= 50:
    print('O valor é R$100,00')
else:
    print('Favor consultar a recepção')

# Expressão condicional (operador ternario)
# Caso a idade seja maior ou igual 18 anos, essa pessoa é maior de idade, caso
# contrario ela é menor de idade
idade = 15

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# Expressão condicional (operador ternario)
'''
sintaxe
    expressão IF condição ELSE expressão
'''    
print('Maior de idade') if idade >= 18 else print('Menor de idade')

# Exemplo 2
possui_passaporte = False

print('Favor embarcar') if possui_passaporte else print('Favor tirar passaporte')


# DESAFIO 🥇
# uso expressão condicional(operador ternário) para criar a seguinte condição
# se velocidade estiver acima de 100 exibir, você foi multado, caso contrário 
# exiba siga em frente
velocidade = 50

print('Você foi multado') if velocidade > 100 else print('Siga em frente')

# LOOP FOR (LAÇO FOR)
for numero in range(1,6):
    print('carregando', numero)

# Exemplo
nomes = ['jeff', 'carl', 'jean', 'luke']

for nome in nomes:
    print(nome)

'''
# Desafio 1  🥇
Usando um loop, exiba na tela: Estamos em X
onde x é um valor iniciando em 18 e finalizando em 110
'''
for x in range(18, 111):
    print('Estamos em', x)
'''
# Desafio 2
# Você precisa de 10 passos para finalizar uma tarefa, exiba na tela, usando loop
#  for a seguinte frase realizando passo x
'''
for tarefa in range(1, 11):
    print('Realizando a tarefa', tarefa)

# fazendo de trás para frente
for tarefa in range(1, 11):
    print('Faltam', 11 - tarefa)

# NESTED LOOPS (LOOPS ANINHADOS)
# Pais + estação

paises = ['brasil', 'india', 'estados unidos']
estacoes_do_ano = ['primavera', 'verão', 'outono', 'inverno']

for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')

for letra in 'Programação':
    print(letra)

# Exemplo
for x in range(1, 11):
    for y in range(1,6):
        print(f'valor externo de {x} e interno de {y}')

'''
# Desafio 1  🥇
Imprima na tela a marca + celular de todos os celulares, usando as informações baixo
'''
celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for marca in celulares:
    for versao in versoes:
        print(f'{marca} {versao}')

# LOOP WHILE
tentativas = 0

while tentativas < 3:
    print('Tente novamente')
    tentativas += 1

# senha
senha = ''

while senha != '123456':
    senha = input('Digite sua senha')
    print('Bem-vindo!')

# Exemplo
# Obrigar a pessoa a digitar algo
nome = ''

while nome == '':
    nome = input('Digite seu nome: ')
    print(f'Bem-vindo {nome}')

# Exemplo 2
horario = 0

while horario <= 17:
    print(horario)
    horario += 1
    print('Hora de ir ver o por do sol')

# Exemplo 3 -  contador regressiva
contador = 100

while contador >= 0:
    print(contador)
    contador -= 1

# DESAFIOS🥇
# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
numero = 1

while numero < 121:
    print(numero)
    numero += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha 
# para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
senha = ''

while senha != 'secreto':
    senha = input('Digite sua senha')

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem 
# descrescente de 100 para 1
contador = 100

while contador >= 0:
    print(contador)
    contador -= 1

# Pass - avisa ao interpretador para seguir adiante e evita o erro de sintaxe do loop
numero = 0

while numero < 5:
    pass

for numero in range(10):
    pass

# Continue - ignorar/pular
for numero in range(100):
    if numero % 2 == 0: # verifica se é par
        print(numero)
    else:
        continue # se não for par, ele permite o loop continuar

# Break - interromper a iteração
# Continue - ignorar/pular
for numero in range(100):
    if numero % 2 == 0: # verifica se é par
        print(numero)
    else:
        break # se não for par, ele interrompe o loop

# Exemplo
frutas = ['Maça', 'Manga', 'Laranja', 'Morango']

# continue
for fruta in frutas:
    if fruta == 'Manga': # quando encontar manga, ele pula e continua o loop
        continue
    print(f'{fruta} adicionada na dieta')

frutas = ['Maça', 'Manga', 'Laranja', 'Morango']

# break
for fruta in frutas:
    if fruta == 'Manga': # quando encontar manga, ele interrompe o loop
        break
    print(f'{fruta} adicionada na dieta')

'''
​# DESAFIOS 🥇

## Desafio 1
Use a operação necessária(break ou continue) para que a seguinte condição aconteça.

* Ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela
estilos = ['Hip-Hop','Rock','Rap','Pop']
'''
estilos = ['Hip-Hop','Rock','Rap','Pop']

for estilo in estilos:
    if estilo == 'Rap':
        continue
    else:
        print(estilo)

'''
## Desafio 2 
Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:

* Ao chegar ao estilo "Rock" a execução deve interrompida 
'''
estilos = ['Hip-Hop','Rock','Rap','Pop']

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)

# FUNÇÕES
'''
SINTAXE
def nome_da_funcao():
    comandos
'''

# Exemplo
def dar_boas_vindas():
    print('Bem-vindo!')

dar_boas_vindas() # chama a função

# Exemplo com parâmetros
def dar_boas_vindas_personalizado(nome): # argumento nome
    print(f'Bem-vindo(a) {nome}')

dar_boas_vindas_personalizado('Saulo')

# Valor/argumento padrão
def apresentar_lugar(lugar='nossa loja'): # argumentos padrões devem estar incluidos no final da lista de argumentos
    print(f'Conheça {lugar}')

apresentar_lugar()

# Dois argumentos padrão 
def apresentar_lugar(horario_funcionamento, lugar='nossa loja'): # argumentos padrões devem estar incluidos no final da lista de argumentos
    print(f'Conheça {lugar}, funcionamento das {horario_funcionamento}')

apresentar_lugar('8:00 as 18:00', 'Disney')

# Desafio🥇

# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome
#  e sobrenome de alguém e dá boas vindas para essa pessoa
def gerar_nome_completo(nome, sobrenome):
    print(f'Bem-vindo(a) {nome} {sobrenome}')

gerar_nome_completo('Saulo', 'Gil')

# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o 
# primeiro o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade
# deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto,
#  multiplicado a quantidade escolhida.
def calcular_valores(preco_produto, quantidade=1):
    print(preco_produto*quantidade)

calcular_valores(1.50, 2)

# PROCESSAR VS RETORNAR
# função que apenas processa dados (imprime na tela)
print('olá')

#função que retorna/armazena valores
cidade = input('Qual a sua cidade') # a fç input permite armazenar o dado em uma variável
'''
Como escolher entre funções que processam vs. retornam dados?
Faça a seguinte pergunta:
Eu vou precisar usar essa informação na lógica do meu programa?
OU
Só preciso processar esse dado, mas não irei utilizar mais ele depois?
'''
# Processa o dado 
def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)

exibir_cotacao_do_dia('usd') # imprime o resultado

# Armazena o dado retornado pela função e processa depois
def obter_cotacao_do_dia(moeda):
    if moeda =='usd':
        return 5.47

cotacao = obter_cotacao_do_dia('usd') # permite armazenar o dado para usar no programa
# exemplo
if cotacao > 5:
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')

# ARGUMENTOS POSICIONAIS VS NOMEADOS
def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')

# Argumento posicional 
exibir_preco('Iphone', 5000) # a ordem interfere!

# Argumento nomeado
exibir_preco(nome_produto='Iphone', preco=5000) # ordem não interfere
exibir_preco(preco=5000, nome_produto='Iphone')
'''
Em argumentos nomeados é possivel determinar que seja obrigatório que o nome do argumento
esteja descrito na função. Para isso, basta usar o * e todos os argumentos após ele deverão 
aparecer nomeados
'''
def exibir_preco(nome_produto,*, preco):
    print(f'{nome_produto} está no valor de: {preco}')

# Argumento posicional 
exibir_preco('Iphone', preco=5000)

# Desafio 🥇
'''
Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:
1 - O primeiro argumento deve ser posicional
2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
'''
def gerar_objeto_personalizado(cor,*, altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalizado('branco',altura=160,formato='quadrado')

# N° de argumentos (posicionais dinâmicos)
def somar(*valores, b): 
    print(valores)
'''
o * indica que vc pode passar varios valores e isso será armazendo em uma tupla
Além disso, o segundo argumento OBRIGATÓRIAMENTE deve estar nomeado na função
'''
somar(10,20,5, b=5)

# Devido o armazenamento em tupla, podemos usar um loop para somar os valores
def somar(*valores, b): 
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar(10,20,5, b=5)

# Kwargs - Keywords arguments **
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
        print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas', d='profissionais')

# Exemplo
def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

fazer_calculo('Jeff',4,6,3,7,a=1,b=2,c=3)

# Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

# Função que irá dentro do decorator
def parabenizar():
    print('Parabens!!!!')

resultado = meu_decorator(parabenizar)
resultado()

# Simplificando o decorator @
# Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator # isso descarta a necessidade de chamar a fç decorator como no exemplo acima
def parabenizar():
    print('Parabens!!!!')

parabenizar()

# Desafio 🥇
'''
Crie um decorator que irá pegar a função que for passado para ele e imprimir o horario atual
antes de executar a função e depois imprimir o horário após ter finalizado a execução da função
    *Dica: você terá que usar o módulo datetime para conseguir o horario atual
'''
from datetime import datetime

def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@monitorar_horario # isso descarta a necessidade de chamar a fç decorator como no exemplo acima
def baixar_musicas():
    print('Baixando músicas')

baixar_musicas()

# COLEÇÕES

# Criando listas com Python

# listas
listas = [10,20,30]
print(listas[0]) # acessando usando o indice

# Descobrir onde  item esta usando o método index
precos = [5,6,3,4,36,2,54,756,231,645,65,21,456,64,32,1]
print(precos[precos.index(4)]) # retorna o valor dentro da lista sem saber o indice
print(precos.index(4)) # retorna o indice do valor passado

# listas no python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1,3,6,'olá', 'café', True, 10.6]
print(itens[4])

# Maneiras diferentes de gerar listas
# Multiplicação de valores (repetição)
lista_de_noves = [9] * 10 # repete o número de nove 9x
print(lista_de_noves)

# com string
lista_de_noves_str = ['nove'] * 10 # repete o número de nove 9x
print(lista_de_noves_str)

# usando gerador range
# 1 a 29
lista_valores_ate_30 = list(range(30))
print(lista_valores_ate_30)

# gerar a partir de um string
print(list('Bem-vindo ao treinamento')) # separa os caracteres

# lista de listas (matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]
print(matriz_de_nomes[0]) # retorna a lista do indice 0
print(matriz_de_nomes[:2]) # retorna as 2 listas internas inteiras
print(matriz_de_nomes[0][0]) # retorna o indice 0 da lista indice 0 = Carol
print(matriz_de_nomes[0][0]) # retorna o indice 0 da lista indice 0 = Carol
print(matriz_de_nomes[1][0]) # retorna o indice 0 da lista indice 1 = Marcus
print(matriz_de_nomes[1][1]) # retorna o indice 1 da lista indice 1 = 50


# Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa 
# durante o dia e imprima ele na tela
objetos = ['celular', 'pc', 'table']
print(objetos)

# Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131
lista_numeros_10_131 = list(range(10,132))

# Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e 
# desafio 2
print(objetos + lista_numeros_10_131)

# Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
# que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 
# uma informação extra, coloque o valor em reais desse objeto também e imprima ele 
# na tela  
matriz = [['celular', 1000],['pc', 5000], ['tablet', 3000]]
print(matriz)

# Encontre valores e manipulacao de itens de uma lista
valores = list(range(1,10))
anos = [2020, 2030, 2040, 2020]

 # Adiciona um valor ao final da lista - append
valores.append(11)
print(valores)

# unir listas
valores.extend(anos) # adiciona no final da listas
print(valores)

# Adicionar lista
nova_lista = valores + anos
print(nova_lista)

# Inserir em uma posição especifica (indice)
print(anos[1]) # indice 1 = 2030
anos.insert(1,2031) # insere um valor no indice indicado no arg 1
print(anos)

# extrair valor com base no indice
print(anos) # indice 1 = 2031; vamos extrair ele!
ano_2031 = anos.pop(1) # retorna o valor (pode ser armazenado em uma variável!)
print(ano_2031)

# remover um valor da lista
print(anos)
anos.remove(2040) # remove o ano 2040 da lista
print(anos)

# outra forma de remover
print(anos)
del anos[2] # deleta o item com indice 2
print(anos)

# o del permite remover uma faixa de valores
print(valores)
del valores[-4:] # deletar anos (elementos da lista anos)
print(valores)

# contar a ocorrencia de um valor em uma lista
valores.append(2) # adicionei mais um 2 na lista
print(valores)
valores.count(2) # conta o número de 2

# resetar uma lista
valores.clear()
print(valores) # retorna lista vazia

# Como ordenar listas simples
valores = [3,6,2,4,9,3,8,1,5,0,5,3]

valores.sort() # ordena de forma crescente
print(valores)

valores.sort(reverse=True) # ordena de forma decrescente
print(valores)

valores.reverse() # inverte a lista
print(valores)

# Trabalhar com multiplas listas usando o ZIP
a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5, 6]

for a,b in zip(a_lista, b_lista):
    print(a)
    print(b)

# exemplo
produtos = ['produto 1', 'produto 2','produto 3','produto 4','produto 5']
precos = [250, 150, 220, 550, 50]

for produto,preco in zip(produtos, precos):
    print(f'O produto {produto} tem o valor {preco}')

# exemplo quando o numero de itens é diferente entre as listas
## precisa usar o zip_longest do módulo itertools
from itertools import zip_longest

titulos = ['Titulo 1','Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descrição 1','Descrição 2', 'Descrição 3']

for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Titulo {titulo} descrição: {descricao}')

# DESAFIOS 🥇
## DESAFIO 1

# Usando as listas abaixo:
produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']
'''
Estamos extraindo preços de um site de produtos e queremos armazenar as informações
encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim
acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e 
valor produto, como as mensagens abaixo:

Produto: Produto 1 encontrado no valor de R$500,00
Produto: Produto 2 encontrado no valor de R$1500,00
Produto: Produto 3 encontrado no valor de R$2700,00
Produto: Produto 4 encontrado no valor de R$5000,00
Produto: Produto 5 encontrado no valor de None  
'''
from itertools import zip_longest

for produto,preco in zip_longest(produtos, precos):
    print(f'Porduto: {produto} encontrado no valor de {preco}')

# Dicionarios
'''
Infos de uma pessoa
    nome
    idade
    altura
'''
pessoa = ['Carol', 18, 1.60, 'Mike', 50, 1.80]
print(pessoa)
# Dicionário (chave, valor)
dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
print(dicionario_pessoa) # facilita a interpretação das infos

# Outra forma de criar dicionário (usando a fct dict)
pessoa_2 = dict(nome='Carol', idade=18, altura=1.60)
print(pessoa_2)

# acessar valores usando a chave
pessoa_2['idade']

# imprimir todas a chaves usando key
print(dicionario_pessoa.keys())

# imprimir todos os valores usando key
print(dicionario_pessoa.values())

# imprimir tanto a chave como o valor
print(dicionario_pessoa.items())

''' Esse tipo de ação é bastante útil para fazer iterações'''
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])

# Tuplas
# ao invés de fazer uma atribuição de valores separados como a seguinte
site1 = 'youtube.com'
site2 = 'facebook.com'
site3 = 'facebook.com'
# ou
valor1 = 23
valor2 = 43
valor3 = 65

# Podemos criar uma tupla
sites = ('youtube.com', 'facebook.com', 'facebook.com')
valores = (23, 43, 65)

# Esse formato permite acessar os valores pelo indice, mas não é possivel alterar
# a tupla como, por exemplo, sort ou adicionar valor
sites[1]
sites[2]
sites[3]
sites[1] = 'saulo' # TypeError: 'tuple' object does not support item assignment
sites.sort() # AttributeError: 'tuple' object has no attribute 'sort'

# tuplas podem ser unidades
dados_dos_sistema = sites + valores
print(dados_dos_sistema)

# Tuplas permitem todos os tipos de dados conforme o exemplo abaixo
tuplas_com_tipos_dados = ('youtube.com', 23, True, 1.2)
print(f'{tuplas_com_tipos_dados[0]} é do tipo {type(tuplas_com_tipos_dados[0])}\n{tuplas_com_tipos_dados[1]} é do tipo {type(tuplas_com_tipos_dados[1])}\n{tuplas_com_tipos_dados[2]} é do tipo {type(tuplas_com_tipos_dados[2])}\n{tuplas_com_tipos_dados[3]} é do tipo {type(tuplas_com_tipos_dados[3])}')

# Arrays - armazena colação de itens de um mesmo tipo
from array import array

'''
link para documentação de arrays
https://docs.python.org/pt-br/3.7/library/array.html
'''

# aceita int, float, str 
numeros = array('i', [1,2,3,4,5,6]) # '1' espeficica o tipo conforme especificado no site, no caso, int
print(numeros)

# permite realizar todas os métodos já vistos
numeros.append(10) # adiciona um valor no final
print(numeros)

numeros.insert(-1, 9) # adiciona item no indice indicado
print(numeros)

numeros.pop(-2) # remove o valor do indice indicado
print(numeros)

numeros.remove(10) # remove o valor indicado
print(numeros)





