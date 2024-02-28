# Ler o número de alunos existentes em umm turma e, após isto, ler as notas destes alunos, calcular e escrever a média aritmética dessas notas lidas. 
notas = []
alunos = int(input('Digite a quantidade de alunos: '))

for i in range(alunos):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas.append(nota)
    print(f'Aluno: {i+1} Nota: {nota}')

somanotas = (sum(notas))
print(somanotas/alunos)