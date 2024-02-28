# Ler 10 valores e escrever quantos desses valores lidos são negativos.

valores = []
valores_negativos = []

for i in range(10):
    valor = float(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

for valor in valores:
    if valor < 0:
        valores_negativos.append(valor)

print(f'Valores negativos lidos: ', valores_negativos)
print(f'Quantidade de valores negativos', len(valores_negativos))