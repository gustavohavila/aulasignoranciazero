class ObjetoGrafico(object):
    def __init__(self,cor):
        self.cor=cor
    def area(self):
        pass
    def perimetro(self):
        pass
    def info(self):
        print('%f metros quadrados serão preenchidos com a cor %s'%(self.area(),self.cor()))

        class cachorro:
            nome='Rex'
            cor='marrom'

        dog=cachorro()
        print(dog.nome)
        print(cachorro.nome)
 #valores estáticos
class Conta(object):
    total=10000
    reserva=0.1
    def __init__(self,ID,saldo):
        self.ID =ID
        self.saldo=saldo
    def deposito(self, valor):
        self.saldo+=valor
        Conta.total+=self.saldo
    def saque(self,valor):
        if self.saldo>=valor:
            self.saldo-=valor
            Conta.total-=valor
    def imprimeReserva():
        print(Conta.total*Conta.reserva)

itau=Conta(123,5000)
itau.deposito(1000)
itau.saque(5000)
print(itau.saldo)
print(Conta.total)
Conta.deposito(itau,4000)
print(itau.saldo)
Conta.imprimeReserva()

#encapsulamento (esconder)
#__
