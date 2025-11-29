#Projeto pokemon
#Nome, ataque=0 a 10,defesa 0 a 10,tipo de ataque: raio, agua, pedra, fogo
#raio aumenta ataque em +2 em relação a tipo agua
#raio tem ataque -3 em tipo pedra
# inseto tem ataque +3 contra tipo raio
#inseto tem ataque -3 contra tipo agua

class Pokemon(object):
    def __init__(self,nome,ataque,raio,dono='sem_dono'):
        self.nome=nome
        self.ataque=ataque
        self.tipo=raio
        self.dono=dono
        print("Pokemon criado, nome: %s" %(nome))
    def atacar(self,ataque):
        self.ataque=ataque
class Treinador(object):
    def __init(self,nome,pokemon='nenhum'):
        self.nome=nome
        self.pokemon=pokemon
        self.lista_pokemon=[pikachu]
    def capturar(self):
        print("Escolha um pokemon para capturar")
        

pikachu=Pokemon('picachuu', 7,3,'raio')
caterpie=Pokemon('caterpie',2,4,'inseto')
jamsie=Pokemon('jamsie',1,1,'fofo')
vulpix=Pokemon('vulpix',8,3,'fogo')
ash=Treinador()
lista_Pokemon=[pikachu,caterpie,jamsie,vulpix]
lista_Treinador=[ash]
#Para herança, super e polimorfismo:
#entender o que o pokemon e o treinador tem em comum (personagem)
#criar a classe super do personagem e criar 2 subclasses (pokemon e treinador)
