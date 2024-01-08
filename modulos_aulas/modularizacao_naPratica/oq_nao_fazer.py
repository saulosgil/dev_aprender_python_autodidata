'''
é comum encontrar scripts gigantes com várias funções.
Essa é um pratica que deve ser evitada!!!
Ao invés, devemos criar módulos especificos para nosso app e deixar o arquivo que 
irá rodar o programa limpo, chamando apenas os módulos e funções
'''
# Exemplo de script com múltiplas funções e infos

class Camera():
  def __init__(self, resolucao_maxima) -> None:
    resolucao_maxima = resolucao_maxima

  def tirar_foto(self):
    print('Tirando foto')

  def aumentar_zoom(self):
    print('Aumentando zoom')
  
  def diminuir_zoom(self):
    print('Diminuindo zoom')

def iniciar_banco_de_dados():
  print('Iniciando conexao')
  print('Criando tabelas iniciais')


def buscar_usuarios():
  print('Buscando usuários')


senhas = 123456
usuarios_maximos = 5