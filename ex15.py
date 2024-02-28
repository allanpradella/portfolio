# ler 3 valores e escrever em ordem crescente
# método mais complexo com manipulação de listas

valores = []
for i in range(3):
    valor = float(input(f'Digite o {i+1}º valor: '))
    valores.append(valor) #Loop adicionando valor à lista [valores]-

valores_odernados = []

while valores:
    min_valor = min(valores) #variável min_valor vai receber o menor dos valores
    valores_odernados.append(min_valor) #o menor valor, será adicionado a lista de valores_ordenados
    valores.remove(min_valor) #depois removerá da lista valores o mínimo valor

print(f'Valores em ordem crescente: ')
for valor in valores_odernados:
    print(valor)