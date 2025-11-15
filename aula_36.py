#variáveis e argumentos(keywords)
"""
def nome(args):
    return

"""
"""
#em algumas situações nao saberei o número de argumentos..

def soma(lista):
    soma_num=0

    for num in lista:
        soma_num+=num
    return soma_num
a=[1,2,3,4]

print(soma(a))

#cOLOCANDO ASTERISCO


def soma(*lista):
    soma_num=0
    print(lista)
    for num in lista:
        soma_num+=num
    return soma_num
a=(1,2,3,4)

print(soma(1,2,3,4,5,6))
"""

#Exemplo de provas
def soma(*nums):
    soma_num=0
    for num in nums:
        soma_num+=num
    return soma_num
def media(p1,p2,p3,peso1,peso2,peso3):
    return (p1*peso1+p2*peso2+peso3*p3)/soma(peso1,peso2,peso3)

print(media(5,4.5,6,1,1,1))
