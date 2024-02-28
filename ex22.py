# Ler o valor N e imprimir todos os valores inteiros entre 1 e N. Considerando N sempre maior que ZERO. 

while True:
    n = int(input(f'Digite um valor: '))
    if n > 0:
        break

for i in range(1, n + 1, 1):
    print(i)
