
# DICIONARIOS ( ou objetos )

cachorro = {
    'Nome': 'Doug',
    'Raça': 'Golden Retriever',
    'Gênero': 'Fêmea',
    'Idade': 2,
    'Saudável': True
}

# forma de acessar um dicionário
print(cachorro['Nome'])
# iterando pelo valor da chave
print(cachorro['Nome'][2])

# reatribuindo valores das chaves existentes
cachorro['Nome'] = 'Doglas'
print(cachorro['Nome'])

# também cria chaves novas
cachorro['Peso'] = 10
print(cachorro)

# removendo chaves junto com seu valor do dicionario
del cachorro['Peso']
print(cachorro)
# só muda a sintaxe do del pro pop()
# removendo elementos baseado na chave
cachorro.pop('Saudável')
print(cachorro)

# fazendo uma copia do meu dicionario cachorro
cachorro_copiado = cachorro.copy()

print(cachorro_copiado)
cachorro_copiado.clear()

print(cachorro_copiado)
print(cachorro)
