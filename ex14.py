# Ler três valores e dizer qual é o maior

v1 = float(input(f'Digite o primeiro valor: '))
v2 = float(input(f'Digite o segundo valor: '))
v3 = float(input(f'Digite o terceiro valor: '))

if v1 > v2 and v1 > v3:
    print(f'O primeiro valor é o maior!')
elif v2 > v1 and v2 > v3:
    print(f'O segundo valor é o maior!')
elif v3 > v1 and v3 > v2:
    print(f'O terceiro valor é o maior!')

