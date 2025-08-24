# Este exercício trabalha com sets (conjuntos) em Python.

frutas = set()           # Cria um set vazio
frutas.add('Maça')       # Adiciona 'Maça' ao set
frutas.add('Banana')     # Adiciona 'Banana' ao set

# Cria uma cópia do set
frutas_copia = frutas.copy()

# Limpa todos os elementos da cópia
frutas_copia = frutas_copia.clear()  

# Imprime o set original e a cópia limpa
print(frutas)       # Mostra: {'Maça', 'Banana'}
print(frutas_copia) # Mostra: None, porque clear() retorna None
