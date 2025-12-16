#

class Quadrados(object):
    def __init__(self,com,fim):
        self.com=com
        self.fim=fim
    def __iter__(self):
        return self
    def __next__(self):
        if self.com<self.fim:
            self.com**2
        else:
            raise StopIteration
x=Quadrados(0,5)

iter(x) is x

x=Quadrados(0,5)
y=Quadrados(0,5)

for i in x:
    print(i)

list(y)

#segunda solução
x=Quadrados(0,5)
l=list(x)

for i in l:
    print(i)

tuple(l)


class Quadrados(object):
    def __init(self,com,fim):
        self.com=com
        self.fim=fim
    def __iter(self):
        return Quadrados_iter(self.com,self.fim)

class Quadrados_iter(object):
    def __init__(self,com,fim):
        self.com=com
        self.fim=fim
    def __next__(self):
        if self.com<self.fim:
            self.com+=1
            return self.com**2
        else:
            raise StopIteration
x=Quadrado(0,5)
for i in x:
    print(i)

list(x)

#solução mais elegante
#usar geradores
class Quadrados4(object):
    def __init__(self,com,fim):
        self.com=com
        self.fim=fim
    def __iter__(self):
        for i in range(self.com+1,self.fim+1):
            yield i**2
x=Quadrados4(0,5)

for i in x:
    print(i)





