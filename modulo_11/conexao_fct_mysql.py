import mysql.connector

def conectar_db(user, password, host, database):
    """Conectar ou criar um banco de dados."""
    conexao = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return conexao

def criar_tabela(conexao):
    """Criar uma tabela Funcionarios."""
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Funcionarios (
            id INT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cargo VARCHAR(255) NOT NULL,
            dataContratacao DATE NOT NULL
        );
    ''')
    conexao.commit()

def inserir_funcionario(conexao, id, nome, cargo, dataContratacao):
    """Inserir um funcionário na tabela Funcionarios."""
    cursor = conexao.cursor()
    query = "INSERT INTO Funcionarios VALUES (%s, %s, %s, %s)"
    valores = (id, nome, cargo, dataContratacao)
    cursor.execute(query, valores)
    conexao.commit()

def listar_funcionarios(conexao):
    """Listar todos os funcionários da tabela Funcionarios."""
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    return cursor.fetchall()

def atualizar_funcionario(conexao, id, novo_cargo):
    """Atualizar o cargo de um funcionário."""
    cursor = conexao.cursor()
    query = "UPDATE Funcionarios SET cargo = %s WHERE id = %s"
    valores = (novo_cargo, id)
    cursor.execute(query, valores)
    conexao.commit()

def deletar_funcionario(conexao, id):
    """Deletar um funcionário da tabela Funcionarios pelo seu ID."""
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Funcionarios WHERE id = %s", (id,))
    conexao.commit()

def fechar_conexao(conexao):
    """Fechar a conexão com o banco de dados."""
    conexao.close()
# ---------------------------------------------------------------------------
# Exemplo de uso:
# ---------------------------------------------------------------------------
conexao = conectar_db('root', 'senhaForte123', 'localhost', 'academia')

criar_tabela(conexao)

# Solicitar dados do usuário e inserir funcionário
id1 = input("Digite o ID do primeiro funcionário: ")
nome1 = input("Digite o nome do primeiro funcionário: ")
cargo1 = input("Digite o cargo do primeiro funcionário: ")
dataContratacao1 = input("Digite a data de contratação do primeiro funcionário (AAAA-MM-DD): ")
inserir_funcionario(conexao, id1, nome1, cargo1, dataContratacao1)


print(listar_funcionarios(conexao))

atualizar_funcionario(conexao, 2, 'Desenvolvedora Sênior')

print(listar_funcionarios(conexao))

deletar_funcionario(conexao, 1)

print(listar_funcionarios(conexao))

fechar_conexao(conexao)