#Comparações e extentendo objetos do python

class Conta:
    def __init__(self,i,s):
        self.ID=i
        self.saldo=s
    def deposito(self,v):
        self.saldo+=v
    def saque(self,v):
        if self.saldo>=v:
            self.saldo-=v
    def __le__(self,outro):
        if self.ID<=outro.ID:
            return True
        return False
    def __eq__(self,outro):
        if self.ID==outro.ID:
            return True
        return False
    def __ge__(self,outro):
        if self.ID>=outro.ID:
            return True
        return False
    def __lt__(self,outro):
        if self.ID<outro.ID:
            return True
        return False
    def __gt__(self,outro):
        if self.ID>outro.ID:
            return True
        return False
    def __ne__(self,outro):
        if self.ID != outro.ID:
            return True
        return False

itau=Conta(123,4000)
bradesco=Conta(123,5000)
print(itau==bradesco)


itau2=Conta(123,4000)

#itau==itau2? false

itau3=itau
itau3.deposito(6)
print(itau.saldo)

#itau==itau3

print(id(itau))


__le__,x<=y
__eq__,x==y
__ge__x>=y
__lt__x<y
__gt__x>y
__ne__


#extendendo objetos
class Banco:
    def __init__(self):
        self.contas=[]
        
class Conta:
    def __init__(self,i,s):
        self.ID=i
        self.saldo=s
    def deposito(self,v):
        self.saldo+=v
    def saque(self,v):
        if self.saldo>=v:
            self.saldo-=v
banco=Banco()
itau=Conta(123,4000)
bradesco=Conta(123,5000)

#Abaixo não funciona, porque não está extendido.
banco.contas.sort()
#ordenando os objetos criados
class Contas(list):
    def sort(self):
        copia=self.copy()
        tam=len(self)
        self.clear()
        while len(self)< tam:
            min_id=copia[0]
            for conta in copia:
                if conta.ID >min_id.ID:
                    min_id=conta
            self.append(min_id)
            copia.remove(min_id)

class Banco:
    def __init(self):
        self.contas=Contas()
santander=Conta(789,6000)
itau=Conta(123,4000)
bradesco=Conta(123,5000)
banco=Banco()
banco.contas.append(itau)
banco.contas.append(bradesco)
banco.contas.append(santander)
banco.contas.sort()

banco.contas
banco.contas[0].ID
banco.contas[1].ID
banco.contas[2].ID
                         






