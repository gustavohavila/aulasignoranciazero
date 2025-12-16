#iteração

#for loops=iteraçao

#qual é o  critério para um objeto ser percorrido por um for loop?

#iterável(iterable)--> capaz de gerar um objeto iterador(iterator).

#__next__=método especial(mágico)

x=open('arquivo'.txt)
for i in x:
    print(i)

x.close()
for i in open('arquivo.txt').readlines():
    print(i)

x=open('arquivo.txt')
x.__next__ #vai percorrer as linhas, e quando a sequencia acabar, vai dar o erro stop interation

y=open('arquivo.txt').readlines()

y.__next__()

y.__iter__()
#list iterator object

z=y.__iter__()

z.__next__()

#next() --> chamar o método do objeto
#iter--> chamar o método next do obj

iter(y) - gera a list iterator

next(z) - passar para a próxima string

x=open('arquivo.txt')
iter(x) is x
True

iter(y) is y
False
#a vantagem é porque é mais rápido, melhor em eficiencia de melhora. É tão rápido quanto linguagem C

for i in open('arquivo.txt').readlines()

x=open('arquivo.txt')

x=iter(x)

while True:
    try:
        i=next(x)
    except StopIteration:
        break
d={'1':1,'2':2,'3':3}
iter(d)
iter(d.keys())

enumerate(['a','b','c'])

x=enumerate('abc')
print(x)

for i in x:
    print(i)
