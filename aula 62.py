class Mamífero:
    def __init__(self, cor_de_pelo, genero,andar):
        self.cor_de_pelo=cor_de_pelo
        self.genero=genero
        self.num_de_patas=andar
    def falar(self):
        print('Olá, sou um mamífero e eu sei falar')
    def andar(self):
        print('Estou andando sobre %i patas'%self.num_de_patas)
    def amamentar(self):
        if self.genero.lower()[0]=='m':
            print("Machos não amamentam")
            return
        print("Amamentando meu filhote")


class Pessoa(Mamífero):
    def __init__(self, cor_de_pelo, genero,andar,cabelo):
        super(Pessoa, self).__init__(cor_de_pelo,genero,andar)
        self.cabelo='Loiro'
    def falar(self):
        super(Pessoa, self).falar()
        print('Olá eu sou uma pessoa e eu sei falar')
    







Rex=Mamífero('marrom','masculino',4)
Rex.amamentar()
Julia=Mamífero('preta','feminino',2)

Julia=Pessoa('preta','feminino',2,'Loiro')
Julia.andar()

Julia.falar()

