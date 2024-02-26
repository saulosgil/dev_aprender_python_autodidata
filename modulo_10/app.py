# Processando itens de uma lista com MAP

# Usando Loops
numeros = []

for i in range(5):
  numeros.append(i)

print(numeros)

# Usando a função MAP - aplica um fct a um vetor/array
nomes = ['larissa', 'Rafael', 'Marcus', 'John']

# Fct que será aplicada
def aprovar_pessoa(nome):
  return nome + ' APROVADO'

# Aplicando a fct no array com MAP
print(map(aprovar_pessoa, nomes)) # precisa converter em lista
print(list(map(aprovar_pessoa, nomes)))