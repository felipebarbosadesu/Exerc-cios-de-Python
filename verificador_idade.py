# Revisão de Logica com py
idade = int(input('Digite a idade: '))
if idade < 12:
    print('Criança')
elif idade > 12 and idade <= 17:
    print('Adolescente')
elif idade > 17 and idade <= 59:
    print('Adulto')
else:
    print('Idoso')
