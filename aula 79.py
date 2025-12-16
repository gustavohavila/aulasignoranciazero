import pickle

arq=open('arquivo.pck','wb')

l1=[1,2,3]
pickle.dump(11,arq)
print(pickle.dumps(11))
class Pessoa:
    def __init__(self,n,p):
        self.n=n
        self.p=p
    def ola(self):
        print('Ola sou %s e peso %s'%(self.n,self.p))


pedro=Pessoa('Pedro',75)
pickle.dump(pedro,arq)
arq.close()
arq=open('arquivo.pck','rb')
x= pickle.load(arq)
print(x)
y=pickle.load(arq)
print(y.n)

arq.close()
