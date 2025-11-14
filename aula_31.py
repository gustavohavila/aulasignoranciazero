
a=[1,2,3,4,5]


n=int(input("Digite o elemento da lista, de 0 a %i" %(len(a)-1)))

print(a[n])

a.remove(n)

print(a)
