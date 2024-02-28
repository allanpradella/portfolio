# Escreva um algoritmo para ler 10 números e ao final da leitura, escrever a soma total dos 10 números lidos.

numeros = []
for i in range(10):
    numero = float(input(f'Digite o {i+1}º valor: '))
    numeros.append(numero)

print(sum(numeros))
