# Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o valor de cada mercadoria. 
# Ao final imprimir o valor total em estoque e a média de valor das mercadorias. 

totalm = int(input(f'Digite a quantidade de mercadorias: '))
mercadorias = []
for i in range(totalm):
    item = float(input(f'Digite o valor da {i+1}º mercadoria: '))
    mercadorias.append(item)

valortotal = (sum(mercadorias))
mediatotal = (valortotal/totalm)

print(f'O valor total em estoque é de {(len(mercadorias))} e a média de valor das mercadorias é de R${mediatotal:.2f}.')