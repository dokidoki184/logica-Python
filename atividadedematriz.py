#faça um programa onde:
#guarde 4 notas de 3 alunos.
#o codigo tem que percorrer a matriz linha por linha 
#para cada aluno, calcule a soma das 4 notas e a media 
#diga se o aluno foi aprovado ou reprovado(media >=6.0)
#e imprima a mdia calculada a se o aluno foi aprovado ou reprovado
nota = [
    [7.0, 8.0, 9.5, 6.2], #aluno 1
    [5.1, 6.9, 7.8, 8.6], #aluno 2
    [9.2, 10.0, 9.0, 10.0] #aluno 3
]
for i in nota:
 numero_aluno = 1
 soma = 0

 for nota in i:
    soma = soma + nota
    media = soma/len(i)

 if media >= 6.0:
     situacao = "Aprovado"

 else: 
    situacao = "Reprovado"

 
 print(f"aluno {numero_aluno}: Média: {media:.2f} - {situacao}")
 
numero_aluno + 1