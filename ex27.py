# Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10, 20] *incluindo os valores 10 e 20 no intervalo e quantos deles estão fora deste intervalo.

valores = []
dentro = []
fora = []

for i in range(10):
    valor = float(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

for valor in valores:
    if (valor >= 10) and (valor <= 20):
        dentro.append(valor)
    else:
        fora.append(valor)
        

print(f'Os valores que estão dentro do intervalo são:  {dentro}.')
print(f'Os valores que estão fora do intervalo são: {fora}.')
