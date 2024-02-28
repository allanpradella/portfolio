# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcule e escreva o percentual que cada um representa em relação ao total de eleitores. 

totaleleitores = int(input(f'Digite o total de eleitores: '))
VB = int(input(f'Digite o total de Votos Brancos: '))
VN = int(input(f'Digite o total de Votos Nulos: '))
VV = int(input(f'Digite o total de Votos Válidos: '))
pb = (VB*100 / totaleleitores)
pn = (VN*100 / totaleleitores)
pv = (VV*100 / totaleleitores)

print(f'Percentual de Votos Brancos: {pb:.2f}%')
print(f'Percentual de Votos Nulos: {pn:.2f}%')
print(f'Percentual de Votos Válidos: {pv:.2f}%')
