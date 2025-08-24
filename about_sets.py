# SETS ( ou conjuntos )

# conjuntos não possuem index em seus elementos 
conjunto = set() # forma para criar um set vazio
conjunto.add('kiwi')
# print(conjunto) 

# iterador do elemento manga
conjunto.update('manga')
# print(conjunto) 

# sets não permitem duplicatas
conjunto_fake = {'kiwi', 'kiwi', 'manga'}
# print(conjunto_fake)

# itens podem ser removidos dos sets
conjunto_fake.remove('manga')
# print(conjunto_fake)

# o pop() remove o primeiro elemento do nosso set
conjunto_fake.pop()
# print(conjunto_fake)
