# #Sintaxe e definição, retorno return 

# Aqui está um **resumo da sua aula de Python** com base nas atividades:

# ---

# ### 📌 Tópicos trabalhados

# 1. **Sintaxe de funções** – uso de `def` para criar funções.
# 2. **Uso do `return`** – retornar valores de dentro da função para serem usados fora dela.
# 3. **Entrada de dados** – utilização de `input()` para receber informações do usuário.
# 4. **Estruturas condicionais** – uso de `if`, `elif` e `else` para tomar decisões.
# 5. **Operações matemáticas** – soma, subtração e multiplicação com funções.

# ---

# ### 📚 Atividades feitas

# 1. **Função de saudação com nome**

#    * Recebe o nome via `input()` e retorna uma mensagem de boas-vindas.

# 2. **Função de saudação por horário**

#    * Recebe um número (hora do dia).
#    * Usa `if/elif/else` para retornar **Bom dia, Boa tarde ou Boa noite**.

# 3. **Função de soma**

#    * Pede dois números e retorna o resultado da soma.

# 4. **Função de subtração**

#    * Pede dois números e retorna a subtração.

# 5. **Função de multiplicação**

#    * Pede dois números e retorna a multiplicação.

# ---

# 👉 Em resumo, a aula mostrou como **criar funções em Python que recebem valores, processam informações e retornam resultados**, aplicando isso em **saudações** e **operações matemáticas básicas**.

# Quer que eu organize esse resumo em um **mapa mental visual** para você memorizar mais fácil?



#Atividade 1
# nome = input('Insira Nome: ')
# def sobrenome(qualquerCoisa):
#     return f'Olá {qualquerCoisa}'
# print(sobrenome(nome))

#Atividade2
# horas = int(input('Digite um horario: '))
# def horario(umhorario): 
#     dia = ''
#     if umhorario >= 5 and umhorario <= 12:
#         dia = 'Bom dia!'
#     elif umhorario >= 13 and umhorario <= 17:
#         dia = 'Boa Tarde!'
#     else: 
#         dia = 'Boa noite!'
#     return dia
# print(horario(horas))

#atividade3
# numero1 = int(input('Numero 1: '))
# numero2 = int(input('Numero 2: '))
# def soma(n1, n2):
#     return n1 + n2
# print(soma(numero1, numero2))

#ativadade4 
# numero1 = int(input('Numero 1: '))
# numero2 = int(input('Numero 2: '))
# def subtrair(n1, n2):
#     return n1 - n2
# print(subtrair(numero1, numero2))

# #atividade 5
# numero1 = int(input('Numero 1: '))
# numero2 = int(input('Numero 2: '))
# def multiplicar(n1, n2):
#     return n1 * n2
# print(multiplicar(numero1, numero2))