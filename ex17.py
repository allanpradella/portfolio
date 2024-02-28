# Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resutlado da divisão do primeiro valor lido
# pelo segundo valor lido. 

a = float(input(f' Digite o 1º valor: '))
b = float(input(f' Digite o 2º valor: '))

while b == 0:
    b = float(input(f' Digite o 2º valor'))

c = a / b
print(c)    