#Projeto pokemon
#Nome, ataque=0 a 10,defesa 0 a 10,tipo de ataque: raio, agua, pedra, fogo
#raio aumenta ataque em +2 em relação a tipo agua
#raio tem ataque -3 em tipo pedra
# inseto tem ataque +3 contra tipo raio
#inseto tem ataque -3 contra tipo agua

lista_evolução=[('Cartepie','Metapod','Buterfree'),('Charmander','Charmeleon','Charizard','Mega Charizard'),('Pichu','Picachu','Raichu'),('Bulbasaur','Ivysaur','Venusaur') ]


class Personagem(object):
    def __init__(self,nome,nível=0):
        self.nome=nome
        self.nível=nível
    

class Pokemon(Personagem):
    def __init__(self,nome,ataque,tipo,dono='sem_dono',nível=0):
        super(Pokemon,self).__init__(nome, nível)
        self.ataque=ataque
        self.tipo=tipo
        self.dono=dono
        print("Pokemon criado, nome: %s" %(nome))
    def atacar(self,ataque):
        self.ataque=ataque
    def evoluir(self):
        pass
class Treinador(Personagem):
    def __init(self,nome,pokemon='nenhum',nível=0):
        super(Treinador,self).__init__(nome,nível)
        self.pokemon=pokemon
        print("Treinador criado, nome: %s" %(nome))
    def capturar(self):
        print("Escolha um pokemon para capturar")


        
#lista de pokemons, depois fazer um banco de dados com todos os pokemons.
pikachu=Pokemon('picachuu', 7,3,'raio')
caterpie=Pokemon('caterpie',2,4,'inseto')
jamsie=Pokemon('jamsie',1,1,'fofo')
vulpix=Pokemon('vulpix',8,3,'fogo')
lista_Pokemon=[pikachu,caterpie,jamsie,vulpix]

#lista de treinadores, depois fazer uma lista com todos os treinadores padrões. Terá um input para criar um novo treinador.
ash=Treinador('Ash')


lista_Treinador=[ash]
#Para herança, super e polimorfismo:
#entender o que o pokemon e o treinador tem em comum (personagem)
#criar a classe super do personagem e criar 2 subclasses (pokemon e treinador)
#pokemon tem nível, personagem tbm.

#Para abstração criar um metodo vazio
#para atributos estaticos, criar valores globais(da classe)
#para encapsulamento, criar encapsulamento de valores que o player naõ precisa acessar.
