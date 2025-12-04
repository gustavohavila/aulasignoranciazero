class Conta:
    def __init__(self,ID,saldo):
        self.ID=ID
        self.saldo=saldo
    def __str__(self):
        return 'ID: %i Saldo:R$ %.2f'%(self.ID,self.saldo)
    def __add__(self,valor):
        self.saldo+=valor


    
