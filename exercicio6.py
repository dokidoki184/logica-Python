#faça um programa onde cria uma lista chamada produtos_preco. e percorra pela lista fazendo conte quantos produtos custam mais de R$ 20,00 calcule o valor total de todos os produtos somados
produtos_preco = [15.99, 25.50, 30.00, 10.00, 5.99, 50.00, 100.00, 59.99, 12.50, 8.75, 99.75]
contador_acima_20 = 0
total = 0 
for preco in produtos_preco:
    total = total + preco
    if preco > 20.00:
           contador_acima_20 = contador_acima_20 + 1
print("Total de produtos acima de R$ 20,00:", contador_acima_20)
print("Valor total dos produtos:", total)


#for preco in produtos_preco:
    #total = total + preco
    #if preco > 20:
        #print(preco, "é maior que R$ 20,00")
    #else:
        #print(preco, "é menor que R$ 20,00")
        #soma = sum(produtos_preco)
#print("Valor total dos produtos:", total)
