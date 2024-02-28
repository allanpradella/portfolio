# Programa para ler a quantidade máxima, mínima e atual de um estoque. Calculando a quantidade média m = (qtd maxi + qtd min /2) Se a qtd atual for maior ou igual a quantidade maior, escrevendo se deve ou não comprar.
qtdmax = float(input(f'Digite a quantidade máxima: '))
qtdmin = float(input(f'Digite a quantidade mínima: '))
qtdatual = float(input(f'Digite a quantidade atual do estoque: '))
mediaestoque = ((qtdmax+qtdmin)/2)

if qtdatual >= qtdmax:
    print(f'Não efetuar compra!')
else:
    print(f'Efetuar compra! ')

