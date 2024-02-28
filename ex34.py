# Imagine que exista um comando chamado 'posiciona x,y' em alguam linguagem onde o X representa a coluna e Y a linha de algo que deve ser impresso. 
# Escreveria a palavra 'olá' na segunda linha da tela, a partir da 10 coluna. Baseado nesta situação escreva um algotitmo, utilizando este comando 'posiciona' citado que senhe na tela um retangulo de 60 colunas ( a paritr da coluna 1 da tela)
# e 10 linhas ( a partir da linha 1 da tela) sendo que a borda desste retângulo será formada pelo caractere '+'. Lembre que somente a primeira e última linha deverão ter todas as colunas preenchidas com o carctere '+'.
# As demais linhas (entre 2 e 9) só terão as colunas 1 e 60 preenchidas. A aparência deste retângulo deve ser parecida com a figura abaixo:

# Desenhar a borda superior
print('posição 1,1', end=' ')
for _ in range(60):
    print('+', end='')
print()

# Desenhar o conteúdo do retângulo
for linha in range(2, 10):
    print(f'posição 1,{linha}', end=' ')
    print('+', end='')
    for coluna in range(2, 60):
        print(' ', end='')
    print('+')

# Desenhar a borda inferior
print('posição 1,10', end=' ')
for _ in range(60):
    print('+', end='')
print()
