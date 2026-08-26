#faça uma atividade que valide a entrada do usuario so quando ele digitar um numero positivo 

numero = int(input("Digite um número positivo: "))
while numero <= 0:
    print("Número inválido. Por favor, digite um número positivo.")
    numero = int(input("Digite um número: "))
print("Você digitou o número positivo:", numero)
