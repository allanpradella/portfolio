# Escreva um algoritmo que imprima a tabuada (de 1 a 10) para os números de 1 a 10.

for i in range(1, 11): #looping para os multiplicadores
    print(f'Tabuada de {i}: ')
    for j in range(1, 11): #looping para os multiplicandos
        resultado = i *j #cálculo entre o multiplicando*multplicador
        print(f'{i} x {j} = {resultado}') #impressão do resultado
        print() #ln para ficar linha em branco 