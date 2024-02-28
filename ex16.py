#ler 3 valores (a,b,c) cada um representando a medida de um triângulo, e escrever se formam ou não um triângulo. obs: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.40

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if ((a < b + c) and (b < a + c) and (c < a + b)):
    print(f'É possível formar um triângulo.')
else:
    print(f'Não é possível formar um triângulo.')

