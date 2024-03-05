import sqlite3

# Conectar-se a um ou criar um banco de dados
conexao = sqlite3.connect('funcionarios.db')
# Criar tabela
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        dataContratacao TEXT NOT NULL
    );
''')
conexao.commit()

# Inserir dados em uma tabela
nome = input('Digite um nome:')
cargo = input('Digite um cargo:')
data = input('Digite uma data no formato aaaa-mm-dd:')

cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)", (1, nome, cargo, data))
conexao.commit()

nome = input('Digite um nome:')
cargo = input('Digite um cargo:')
data = input('Digite uma data no formato aaaa-mm-dd:')

cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)", (2, nome, cargo, data))
conexao.commit()

# Listar todos os dados de uma tabela
cursor.execute("SELECT * FROM Funcionarios")
funcionarios = cursor.fetchall()
print(funcionarios)

# Alterar dados de uma tabela
cursor.execute("UPDATE Funcionarios SET cargo = ? WHERE id = ?",('Desenvolvedor Sênior', 2))
conexao.commit()

# Excluir dados de uma tabela
cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (1,))
conexao.commit()

# Obrigatório, no caso do SQlite, fechar a conexão, após finalizar operações
conexao.close()
