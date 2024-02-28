# Ler duas notas do aluno, calculara média e dizer se ele foi aprovado ou não. Considerando aprovado se a nota for maior que 7. 
n1 = float(input(f'Digite a primeira nota do aluno: '))
n2 = float(input(f'Digite as egunda nota do aluno:'))
media = (n1 + n2) / 2
if media >= 7:
    print(f'O aluno foi aprovado. Sua média é de {media}.')
else:
    print(f'O aluno não foi aprovado. Sua média é de {media}.')

