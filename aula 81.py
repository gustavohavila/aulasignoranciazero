#compressão de listas

l=[x+10 for x in range(10)]
"""
l=[]
for i in range(10):
    l.append(i+10)
print(l)
"""
m=[x for x in range(10)]
print(m) #0 a 10

#velocidade de C

"""
a=open('ex.py')
l=a.readlines()
l=[linha.rstrip() for linha in l]
"""
#l=[linha.rstrip() for linha in open('ex.py')]

#eficiente em memória e processamento

l=[]
for i in range(10):
    if i%3==0:
        l.append(i)
import random
l=[random.randint(1,100) for i in range(30) if i%2==0]
print(l)

l=[random.randint(1,100) for i in range(30)]
l=[x for x in l if x%2==0]
print(l)


#NESTED FOR LOOP##
l=[x+y+z for x in 'abc' for y in 'lmn' for z in 'xyz']
print(l)
#sintaxe equivalente:
for x in 'abc':
    for y in 'lmn':
        l.append(x+y)
