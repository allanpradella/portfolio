# Acrescentar uma mensagem de 'Valor Inválido' no exercício 17 caso o segundo valor informado seja ZERO. 

a = float(input(f'Digite o primeiro valor: '))

while True:
    b = float(input(f'Digite o segundo valor: '))
    if b != 0:
        break
    else:
        print('Valor Inválido')

print(a/b)