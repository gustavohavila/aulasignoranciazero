"""numeros=[1,2,3,6]
for i in numeros:
    print(i)

ALUNOS=10

medias=[]

for i in range(1,ALUNOS+1):
    notas=0
    for j in range (1,5):
        notas+= float(input("Digite a nota %i de 4 do aluno %i de %i: "%(j,i,ALUNOS)))

    notas/=4
    medias.append(notas)
num =0

for media in medias:
    if media>= 7.0:
        num+=1
print("O número de alunos com média maior que 7 é ", num)
"""

i=1
elementos=[]
maiores=[]
pares=[]
while i!= -1:
    i=int(input("Entre com o novo elemento"))
    elementos.append(i)
    if i>10:
        maiores.append(i)
    if i%2==0:
        pares.append(i)

print("os elmentos que são maiores que 10",maiores)
print("os elmentos que são maiores que sao pares",pares)
