# # Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o valor de cada mercadoria. 
# Ao final imprimir o valor total em estoque e a média de valor das mercadorias. 

# Não é necessário informar a quantidade, mas sim se tem ou não alguma mercadoria a mais. 

mercadorias = []
estoque = []

while True:
    item = float(input('Digite o valor do Item: '))
    mercadorias.append(item)
    print('Item adicionado.')
    estoque_atual = sum(mercadorias)
    estoque.append(estoque_atual)

    a = input('Gostaria de adicionar outro item? S/N: ')
    if a.lower() != 's':
        break

media_mercadorias = sum(mercadorias) / len(mercadorias)
print(f'Há {len(mercadorias)} itens e a média das mercadorias é de R${media_mercadorias:.2f}.')
