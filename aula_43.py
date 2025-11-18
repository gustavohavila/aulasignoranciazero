#Statements break e continue

#break -->parar ou interromper
"""
for i in range(10):
    if i==5:
        break
    print(i)

i=0
n=10

while i<n:
    i+=1
    if i==5:
        break
    print(i)

for i in range(10):
    for j in range(10):
        if j==5:
            break
        print(i,j)


def criaLista():
    lista=[]
    m=int(input("Digite o tamanho da lista"))
    for i in range(m):
        ele=float(input("Digite o elemento %i de %i"%(i+1,m)))
        lista.append(ele)
    return lista
def main():
    l1=criaLista()

    n=int(input("Digite o número de elementos que se deseja somar:"))
    soma=0
    for i in range(len(l1)):
        if i==n:
            break
        soma+=l1[i]
    print("A soma é",soma)

main()
"""
#continue

for i in range(10):
    if i==5:
        continue
    print(i)
