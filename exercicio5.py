#faça um programa onde: a variavel guarde,  oito indices diferentes onde o codigo percorra a lista com for e imprima para cada idade, se a pessoa e menor de idade (<18) ou maior de idade (>=18).
idade = [12, 15, 17, 19, 22, 30,  25, 10]
for i in idade:
    if i < 18:
        print(i, "é menor de idade")
    else:
        print(i, "é maior de idade") 