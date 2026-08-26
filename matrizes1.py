matriz = [
    [6, 7, 5],
    [10, 98, 67],
    [65, 89, 23]
]

for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            print(valor, "é par")
        else:
            print(valor, "é ímpar")
