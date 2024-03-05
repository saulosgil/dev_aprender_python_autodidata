import sqlite3

# Conectar-se a um ou criar um banco de dados
def conectar_db(nome_db):
    conexao = sqlite3.connect(nome_db)
    return conexao

# Criar tabela
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE Funcionarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            dataContratacao TEXT NOT NULL
        );
    ''')
    conexao.commit()

# Inserir dados em uma tabela
def inserir_funcionario(conexao, id, nome, cargo, dataContratacao):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",
                   (id, nome, cargo, dataContratacao))
    conexao.commit()

# Listar todos os dados de uma tabela
def selecionar_todos_funcionarios(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    return cursor.fetchall()

# Alterar dados de uma tabela
def atualizar_funcionario(conexao, id, cargo):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Funcionarios SET cargo = ? WHERE id = ?",
                   (cargo, id))
    conexao.commit()
# Como excluir dados de uma tabela
def deletar_funcionario(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (id,))
    conexao.commit()

# -----------------------------------------------------------------------------------
# Usando as funções
# -----------------------------------------------------------------------------------
conexao = conectar_db('funcionarios.db')

# Criar uma tabela
criar_tabela(conexao)

# Exemplo de como receber dados do usuário na sua aplicação e depois passar para o banco de dados
nome = input('Digite um nome:')
cargo = input('Digite um cargo:')
data = input('Digite uma data no formato aaaa-mm-dd:')

inserir_funcionario(conexao, 1, nome, cargo, data)
inserir_funcionario(conexao, 2, nome, cargo, data)

# Exemplo de uso da tabela que pesquisa e retorna dados de uma tabela
print(selecionar_todos_funcionarios(conexao))  # Imprime todos os funcionários

# Exemplo de uso da função de alterar dados de uma tabela
atualizar_funcionario(conexao, 2, 'Desenvolvedora Sênior')

# Exemplo de como retornar dados que foram retornados do banco de dados
print(selecionar_todos_funcionarios(conexao))  # Imprime todos os funcionários após a atualização

# Exemplo de uso da função de exclui um usuário
deletar_funcionario(conexao, 1)

# Exemplo de uso da tabela que pesquisa e retorna dados de uma tabela
print(selecionar_todos_funcionarios(conexao))  # Imprime todos os funcionários após a deleção

# Obrigatório, no caso do SQlite, fechar a conexão, após finalizar operações
conexao.close()