matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
print(matriz[1][1]) #acessar o elemento da matriz

#for linha in matriz:
    # for valor in linha:
            #print(valor)

for i in range(len(matriz)):
  for j in range(len(matriz[i])):
    print("linha", i, "coluna", j, "-> valor", matriz[i][j])

#range e para chamar mais de um elemento