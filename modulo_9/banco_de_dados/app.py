# SQL - Structure Query Language
#db.sqlite3
import sqlite3

with sqlite3.connect('modulo_9/banco_de_dados/artistas.db') as conexao:
  # criar uma conexao com o banco de dados
  sql = conexao.cursor()

  # rodar comando SQL - create
  sql.execute('create table banda(nome text, estilo text, membros interger);')
  
  # exemplo de inserir dados
  sql.execute('insert into banda(nome, estilo, membros) values ("Banda 1", "Rock", 3);')
  
  # exemplo de usar dados de uma aplicação em um comando SQL
  nome_da_banda = input('Digite o nome da banda: ')
  c = input('Digite o estilo da banda: ')
  quantidade_integrantes = int(input('Quantidade de integrantes da banda: '))

  sql.execute('insert into banda values(?, ?, ?)', [nome_da_banda, nome_da_banda, quantidade_integrantes])

  # Salvando alterações no banco de dados
  conexao.commit()

# Exibir dados no consolo python
bandas = sql.execute('select * from banda;')

for banda in bandas:
  print(banda)







