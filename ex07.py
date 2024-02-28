# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considere que a média é poderada e que o peso das notas é 2, 3 e 5. Formula para o cálculo:
# MEDIAFINAL = (N1* 2 + N2 *3 + N3 *5) /10
n1 = float(input(f'Digite a primeira nota do aluno: '))
n2 = float(input(f'Digite a segunda nota do aluno: '))
n3 = float(input(f'Digite a tereceira nota do aluno:'))
mediafinal = ( n1 * 2 + n2 * 3 + n3 * 5 ) / 10
print(f'A média ponderada do aluno é de {mediafinal}.')