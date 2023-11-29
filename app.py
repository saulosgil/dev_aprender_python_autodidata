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




