#matrizes
#Escreva uma função que recebe um inteiro m e outro n e com isso constroi uma
#matriz mxn

matriz=[]

m=int(input("Digite o número de linhas da matriz: "))
n=int(input("Digite o número de colunas da matriz: "))

def constroiMatriz(m,n,matriz):
    for i in range(1,m+1):
        linha=[]
        for j in range(1,n+1):
            x=int(input("Digite o elemento %i%i da matriz: " %(i,j)))
            linha.append(x)

        matriz.append(linha)



def TrocaElemento(pos1,pos2,matriz):
    elemento1=matriz[pos1[0]] [pos1[1]]
    elemento2=matriz[pos2[0]] [pos2[1]]
    matriz[pos1[0]] [pos1[1]] =elemento2
    matriz[pos2[0]] [pos2[1]] =elemento1

constroiMatriz(m,n,matriz)
pos1=int(input("Digite a posição do elemento 1"))
pos2=int(input("Digite a posição do elelemnto 2"))
