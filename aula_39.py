#recursividade
"""
def fatorial(n):
    fat=1
    for i in range(1,n+1):
        fat*=i
    return fat


def fatorial(n):
    if n==1:
        return n
    return fatorial(n-1)*n
print(fatorial(5))



def imprimir(x,y):
    print(x)
    if x==y:
        return x
    return imprimir(x+1,y)

imprimir(2,10)
"""

def soma(n):
    if n==0:
        return n
    return soma(n-1)+n
