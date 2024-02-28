# Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

valores = []
for i in range(10):
    valor = float(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

print(f'A soma dos valores é',sum(valores))
print(f'A média aritmética dos valores é de',(sum(valores)/10))