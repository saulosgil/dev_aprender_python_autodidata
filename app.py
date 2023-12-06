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
print('arquivo localizado em \c:drive\\arquivo1.txt') # exemplo para retirar o código identificado (\a)

# Preferencialmente salvar string em variaveis
nome = 'Saulo'
print(nome)

# veriricar tamanho da string
print(len(nome))

# DESAFIO
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

# DESAFIO 
nome = 'Carol'
hobby = 'ouvir música'

# Imprimir 'Olá, sou a Carol e gosto de ouvir música'
print(f'Olá, sou a {nome} e gosto de {hobby}.')

# DESAFIO
## monte a seguinte palavra, usando as sílabas como base
b = 'ba'
parte2 = 'nica'
a = 'a'
r = 'ri'
parte1 = 'eletrô'
t = 'te'

# Imprimir 'bateria eletrônica'
print(f'{b}{t}{r}{a} {parte1}{parte2}')

# Packing
a,b,c,d = 1,2,3,4
print(a)
print(b)
print(c)
print(d)

# DESAFIO
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
print(nome_curso_strip.lstrip()) # remove os espaços a esquerda
print(nome_curso_strip.rstrip()) # remove os espaços a direita
print(nome_curso.find('ção')) # identifica o indice da primeira string indicada
print(nome_curso.replace('Vídeo', 'Música')) # identifica a string do primeiro argumento e troca pela segunda no segundo argumento

# DESAFIO
# Através da criação de string dinâmico e os métdoso de um string que acabou de 
# aprender, use como base as variáveis a seguir para criar as seguintes frases:

print('É melhor FEITO que PERFEITO') 

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

# resposta

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
print('É melhor FEITO que PERFEITO') 

# Slice, Extraindo partes de um String
teclado = 'teclado'

print(teclado[2]) # acessa o indice 2, no caso c
print(teclado[-1]) # acessa o indice a partir do último elemento, no caso -1 = o
print(teclado[-3]) # acessa o indice a partir do último elemento, no caso a

# identificando o indice de uma string pelo método .index
print(teclado.index('t')) 

# acessando a última ocorrência de um caracter
frase = 'Clean Code'

print(frase.rindex('C')) # pega a segunda ocorrência do caracter passado como argumento

# acessando partes de uma string
link = 'facebook.com/devaprender'

print(link[0])
print(link[-1])
print(link[0:5]) # o último indice não é inclído!
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

# DESAFIO 1: Encontre o índice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'

# respostas
print(biblioteca[5])
print(biblioteca[-5])
print(biblioteca[biblioteca.index('o')])

# DESAFIO 2
# usando a frase 'Desenvolvimento De Aplicações', imprima apenas 'De Aplicações'
var = 'Desenvolvimento De Aplicações'

# resposta
print(var[16:])
print(var[var.rindex('D'):])

# SPLIT E JOIN

frase = 'Olá, bem-vindo a este treinamento!'

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

# DESAFIOS

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

# DESAFIO 1: transforme a frase1 em uma lista de palavras e guarde o resultado em
# uma variável chamada palavras 2
palavras1 = frase1.split()
palavras1

# DESAFIO 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em
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
print(type(senha)) # a resposta sempre é uma str

quantidade_de_filmes = int(input('Quantos filmes você viu esse mês? '))
print(type(quantidade_de_filmes))

