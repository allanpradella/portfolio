# Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, e dias e escreva a idade dessa pessoa express em dias: considere o ano tendo 365 dias e o mês 30 dias.

idade = int(input('Digite a idade: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))
idadedias = ((idade*365) + (meses*30) + (dias))
print(f'A idade é de {idadedias}')