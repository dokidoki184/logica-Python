#faça um programa que receba N numeros DIGITADOS PELO USUARIO, onde ele tem que me dizer quantos NUMEROS PARES E IMPARES foram digitados.



par = 0
impar = 0
for i in range(1, 10):
    numero = int(input("digite um numero: "))
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print("quantidade de numeros pares: ", par)
print("quantidade de numeros impares: ", impar)