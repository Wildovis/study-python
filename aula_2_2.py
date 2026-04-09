produtos=[]
produtos.append('suco')# append serve para adicionar a lista
produtos.append('detergente')
produtos.append('chocolate')
produtos.append('refrigerante')
produtos.append('sacola')
produtos.append('bucha')
print(produtos)
print(produtos[0]) # produtos 0 serve para retornar o primeiro produtos
print(produtos[2])
print(produtos[2:4]) # traz o filtro entre os produtos 2 e 4
print(produtos[4:])
print(produtos[:4])
print(produtos[4])
for i in range (len(produtos)): # for forma de percorrer cada produto da lista com indice
    print(produtos[i])
print(produtos[2])
for produto in produtos : # for forma de percorrer cada produto da lista
    print(produto)
for i in range(len(produtos)):
    print(produtos[i])
