# o mesmo código que o ex17.py mas utilizando o método DO 
a = float(input(f'Digite o primeiro valor: '))

while True:
    b = float(input(f'Digite o segundo valor: '))
    if b != 0:
        break
    else:
        print(f'O segundo valor não pode ser zero. Digite novamente o segundo valor: ')

total = a / b
print(f'O valor da divisão do primeiro sobre o segundo é de {total}.')