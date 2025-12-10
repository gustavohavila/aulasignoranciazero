#del --> delete --> deletar/apagar

x=10
del x
try:
    print(x)

finally:

    l=[1,2,3]

    del l[2]

    print(l)

t=1,2,3

del t[2]

s='string'
del s[4]

d={'1':1,'2':2,'3':3}

class Pessoa(object):
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def nome2(self):
        print('ola eu sou o',self.nome)
joao=Pessoa('Joao',23)
del joao.nome
joao.nome
del joao.nome2()


#is vem do ingles é

[1,2,3]==[1,2,3]

[1,2,3]is[1,2,3] #vai dizer uqe não é.. pq e mais profundo.
def __eq__ #vai fazer comparaçaõ entre os IDs das listas.
l1=[1,2,3]
l2=l1

l1 is l2 #TRUE
