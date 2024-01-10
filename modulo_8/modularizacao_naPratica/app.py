'''
Com os módulos organizados, basta chamar eles e suas funções
'''
from banco_de_dados import iniciar_banco_de_dados, buscar_usuarios
from configuracoes import senhas, usuarios_maximos
from processamento_imagem import Camera 

'''
Agora seria necessário apenas aplicar as funções (não criar tudo neste script!!)
'''

# teste das funções do móculo banco de dados
iniciar_banco_de_dados()
buscar_usuarios()