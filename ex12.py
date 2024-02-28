# Faça um algoritmo para ler número da conta do cliente, saldo, débito e crédito. Após calcular e escrever o saldo atual. Também testar se o saldo atual for maior ou igual a zero e escrever a mensagem saldo neg ou posi.

nconta = float(input(f'Digite o número da conta: '))
saldo = float(input(f'Digite o saldo: '))
debito = float(input(f'Digite o débito(despesa): '))
credito = float(input(f'Digite o crédito(entrada): '))
saldoatual = (saldo + credito - debito)

if saldoatual >= 0:
    print(f'Saldo positivo!')
elif saldoatual == 0:
    print(f'Sem saldos...')
else: 
    print(f'Saldo negativo!')

print(f'O saldo é de {saldoatual}.')