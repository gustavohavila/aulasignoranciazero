class Minha:
    def __init__(self):
        self.x=0
        self.y=0
meu=Minha()
#print(meu.x)
meu.x=5
#print(meu.x)
meu.z=1
#print(meu.z)


#Associações
class PessoaS2Animais:
    def __init__(self,nome,peso,cao):
        self.nome=nome
        self.peso=peso
        self.cao=cao
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()
class Cachorro:
    def __init__(self, nome,cor):
        self.nome=nome
        self.cor=cor
    def daApatinha(self):
        print('%s extendeu a patinha' %self.nome)
    def latir(self):
        print('AUAUAUAUAUAU')
    
rex=Cachorro('Rex','marrom')
pedro=PessoaS2Animais('Pedro',75,rex)
pedro.treinar()
print(pedro.cao.cor)
