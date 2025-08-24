# Este exercício pede ao usuário que digite 3 números.  
# Para cada número digitado, o programa verifica se ele é par ou ímpar  
# usando o operador módulo (%) e imprime o resultado correspondente.

for i in range(3):
    valor = int(input('Digite um número: '))
    
    if valor % 2 == 0:
        print(f'O número {valor} é PAR')
    else:
        print(f'O número {valor} é ÍMPAR')
