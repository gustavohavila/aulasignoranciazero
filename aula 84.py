#gerador

def geraQuadrados(n):
    for i in range (n):
        yield i**2

for i in geraQuadrados(5):
    print(i)

x=geraQuadrados(5)
list(x)
iter(x)#True
y=geraQuadrados(5)
next(y)
next(y)

for i in [x**2 for x in range(5)]:
    print(i)


#geradores tem economia de memoria e pode ser convertido em lista, tupla, dicionário

def imprime(n):
    for i in range(n):
        x=yield i**2
        print(x)
z=imprime(5)
next(x)
z.send(5)#enviando 5-para x
