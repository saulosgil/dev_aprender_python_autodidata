'''
Neste script o projeto foi refatorado com o uso de funções'''
'''
# Desafio 🥇
#### Dicas Iniciais
    * Crie uma nova turtle primeiro
    * Coloca seu programa em loop 
    * Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás
    * Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos
    * Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta
    * Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados
    * Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.

#### Dicas Adicionais

    * Não esqueça de converter o input do usuário para o tipo apropriado
    * Resolva um problema de cada vez e lembre de seguir a seguinte lógica: 
Pergunte -> Processe resposta -> A
'''

### Desafio 1 -Monte um mini-game turtle, que possibilite que o usuário controle 
# para qual direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado
#  a cada nova movimentação

# importar biblioteca
from turtle import Turtle

# inicializa uma turtle
t = Turtle()

# Defini velocidade
t.speed(1)

# obter distancia 
def obter_distancia():
    distancia = int(input('Quantos pixels devemos movimentar para a frente?'))
    return distancia

# rotacionar sim ou não
def rotacionar_turtle(turtle):
    movimentar_para_lado = input('Rotacionar?\n Digite d para direta\n Digite e para esquerda\n Digite n para não rotacionar')
    if movimentar_para_lado == 'd':
        rotacionar_para_direita(turtle)        
    elif movimentar_para_lado == 'e':
        rotacionar_para_esquerda(turtle)

# rotacionar para direita
def rotacionar_para_direita(turtle):
    angulo = int(input('Quantos graus para a direta devemos rotacionar?'))
    t.right(angulo)

# rotacionar para esquerad
def rotacionar_para_esquerda(turtle):
    angulo = int(input('Quantos graus para a direta devemos rotacionar?'))
    t.left(angulo)

# Programa
while True:
    direcao = input('Para qual direção devemos ir?\n Digite f para frente\n Digite t para trás')
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)        
        t.forward(distancia)        
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('Continuar andando?')
    if resposta not in ('sim', 's'):
        break
'''
### Desafio 2 
Usando o mini-game, desenha um quadrado passando instruções para a turtle, 
totalmente através do input do usuário
'''