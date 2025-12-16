#zip,map, filter
"""
#zip

#help(zip)

l1=[1,2,3]
l2=[4,5,6]


a=zip(l1,l2)
list(a)
print(list(a))

l3=[7,8,9]

print(list(zip(l1,l2,l3)))


l1=['ovos','presunto','frango']
l2=[5,2,3]

a=zip(l1,l2)

for i in a:
    print(i)

a.__next__
"""

#Indo para o MAP

#requer uma função e quantos interáveis são necessários

#gera um iterador de quantos valores
l=[x**2 for x in range(4)]
l1=map((lambda x:x**2), range(4))
print(l)
print(list(l1))

l1=map((lambda x,y:x+y), range(4),range(3,-1,-1))
print(list(l1))
#[3, 3, 3, 3]

def soma(x,y):
    return x+y
l2=map(soma,range(4),range(3,-1,-1))
l1=[soma(x,y) for x in range(4) for y in range(3,-1,-1)]
print(l1)
#maps são mais rápidos do que for loop convencional
#list compreension é mais rápido do que map

#mas map pode retornar qualquer função.

[x for x in range(5) if x%2==2]


#filter

a=filter((lambda x:x%2==0),range(5))
print(list(a))

