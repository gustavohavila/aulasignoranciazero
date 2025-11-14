#regras
#digita o numero de inimigos, o programa gera 
# a cada rodada, é mostrada a vida e SP.
#escolher a opçao 1 ou 2
#Escolhendo 1:
#causa 10 a 15(aleatoriamente) de dano a um inimigo aleatório    
#depois percorrer cada um dos inimigos causando dano ao player entre 1 a 3.
#mas existe 25% de chance de errar o ataque.
#reimprime a vida e SP do player

#Se escolher cura, tem que saber que tem que ter mais de 10 de SP,
#pois cura consome 10 de SP
#e recebe vida entre 10 e 15.
#a cada rodada recebe 3 de sp. Mas o SP não passa de 100.

#O JOGO ACABA QUANDO MATAR TODOS OS INIMIGOS OU QUANDO VC FOR MORTO.
#Jogo simples de ataque e cura
#importa o módulo random
import random

#armazena a vida do player
player_vida=500

#armazena o sp do player
player_sp=100

#vida padrão de um inimigo
inimigo_vida=50

#determina o número de inimigos
n=int(input("Digite o número de inimigos:"))

#vetor que armazena todos os inimigos
inimigos=[]
#vetor de vida de cada inimigo
vida_inimigos=[]



contador_mortos=0
for i in range(n):
    inimigos.append(i)
    vida_inimigos.append(inimigo_vida)



print("Informações gerais do jogo:")
print("player_vida",player_vida)
print("player_sp",player_sp)
print("inimigo_vida",inimigo_vida)
print("Vida_inimigos",vida_inimigos)
#rodada de ataqu
while player_vida>0 or contador_mortos==n:
    opção=int(input("Digite atacar (1) ou curar (2):"))
    print('')
    if opção ==1:
        inimigo_machucado=random.randint(1,len(inimigos))
        vida_inimigos[inimigo_machucado-1]
        dano_aleatorio=random.randint(10,15)
        print("Causou %i de dano ao inimigo %i !"%(dano_aleatorio, inimigo_machucado))
        vida_inimigos[inimigo_machucado-1]-=dano_aleatorio
        for i in range(len(inimigos)):
            chances=[0,1,2,3]
            dano_individual=random.choice(chances)
            print("Inimigo %i causou %i de dano!"%(i+1,dano_individual))
            player_vida-=dano_individual
        
        print("player_vida",player_vida)
        print("player_sp",player_sp)
    if opção==2:
        if player_sp<=10:
            print("SP insuficiente")
        elif player_sp>90:
            print("Sp já chegou no limite")
        else:
            player_vida+=random.randint(10,15)
            player_sp-=10
            if player_sp>99:
                player_sp=100
        print("player_vida",player_vida)
        print("player_sp",player_sp)
    if player_sp<97:
            player_sp+=3
    #inimigos mortos
    for i in range(len(inimigos)):
        if vida_inimigos[i]<=0:
            contador_mortos+=1
            print("Inimigos mortos: ",contador_mortos)

    if player_vida<0:
        print("PLAYER MORREU")
    if contador_mortos>n:
        print("Inimigos mortos, player venceu")
    
    print('')
    print("Informações gerais do jogo:")
    print("player_vida",player_vida)
    print("player_sp",player_sp)
    print("inimigo_vida",inimigo_vida)
    print("Vida_inimigos",vida_inimigos)
    print('')
