# Este arquivo contém exercícios de Python sobre funções, retorno de valores e operações básicas.

# --- Atividade 1: Saudação com nome ---
nome = input('Insira o nome: ')

def saudacao_nome(nome_usuario):
    return f'Olá {nome_usuario}'

print(saudacao_nome(nome))

# --- Atividade 2: Saudação por horário ---
horas = int(input('Digite um horário: '))

def saudacao_horario(horario):
    if 5 <= horario <= 12:
        return 'Bom dia!'
    elif 13 <= horario <= 17:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

print(saudacao_horario(horas))

# --- Atividade 3: Soma de dois números ---
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

def soma(n1, n2):
    return n1 + n2

print(soma(numero1, numero2))

# --- Atividade 4: Subtração de dois números ---
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

def subtrair(n1, n2):
    return n1 - n2

print(subtrair(numero1, numero2))

# --- Atividade 5: Multiplicação de dois números ---
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

def multiplicar(n1, n2):
    return n1 * n2

print(multiplicar(numero1, numero2))
