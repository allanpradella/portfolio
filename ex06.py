# Uma revendedora de carros usados paga a seus funcionários vendidos um salário fixo por mês, mais uma comissão fixa por carro vendido e mais 5% sobre o total de vendas efetuadas.
## Escreva um algoritmo que leia o número de carros vendidos, o valor total da vendas, o valor que ele recebe por cada carro e o salário fixo e calcule o salário. 
salariofixo = float(input(f'Digite o salário fixo: '))
carrosvendidos = int(input(f'Digite a quantidade de carros vendidos: '))
percentualcomissao = float(input(f'Digite o percentual da comissão:'))
valorcarro = float(input(f'Digite o valor dos carros: '))
comissao = (carrosvendidos*valorcarro) * (percentualcomissao / 100)
vendas = (comissao*(5/100))
salariofinal = (salariofixo + comissao + vendas)
print(f'Foram vendidos {carrosvendidos} carros e a comissão da venda dos carros é de {comissao}. A comissão sobre as vendas é de {vendas} e o Salário final é de {salariofinal}.')
