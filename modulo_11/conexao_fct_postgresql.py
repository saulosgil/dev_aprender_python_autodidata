import psycopg2

def conectar_db(dbname, user, password, port, host='localhost'):
    conexao = psycopg2.connect(
        dbname=dbname, 
        user=user, 
        password=password,
        port=port,
        host=host
    )
    return conexao


def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Funcionarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cargo VARCHAR(255) NOT NULL,
            datacontratacao DATE NOT NULL
        );
    ''')
    conexao.commit()

def inserir_funcionario(conexao, nome, cargo, datacontratacao):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO Funcionarios (nome, cargo, datacontratacao) VALUES (%s, %s, %s)",
        (nome, cargo, datacontratacao)
    )
    conexao.commit()

def atualizar_funcionario(conexao, id, novo_cargo):
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE Funcionarios SET cargo = %s WHERE id = %s",
        (novo_cargo, id)
    )
    conexao.commit()

def deletar_funcionario(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Funcionarios WHERE id = %s", (id,))
    conexao.commit()

def listar_funcionarios(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    return cursor.fetchall()

# Exemplos de uso:
conexao = conectar_db('railway', 'postgres', 'Y4EVahgoeOcJHhyEsi2m', '7126', 'containers-us-west-32.railway.app')


criar_tabela(conexao)

nome = input("Informe o nome do funcionário: ")
cargo = input("Informe o cargo do funcionário: ")
datacontratacao = input("Informe a data de contratação (AAAA-MM-DD): ")

inserir_funcionario(conexao, nome, cargo, datacontratacao)

id_atualizar = input("Informe o ID do funcionário que você deseja atualizar: ")
novo_cargo = input("Informe o novo cargo para este funcionário: ")

atualizar_funcionario(conexao, id_atualizar, novo_cargo)

id_deletar = input("Informe o ID do funcionário que você deseja deletar: ")

deletar_funcionario(conexao, id_deletar)

print(listar_funcionarios(conexao))

conexao.close()