# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.
salario = float(input(f'Digite o valor do salário atual do funcionário: '))
percentual = float(input(f'Digite o percentual de aumento: '))
reajuste =  (salario + (percentual*salario/100))
print(f'O novo salário será de {reajuste}')