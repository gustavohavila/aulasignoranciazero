
"""n=int(input("Digite o valor de N"))
5
5*4*3*2*1
fatorial=n
for i in range (1, n,1):
    fatorial*=i
    i=i-1
    print(fatorial)
print(fatorial)



for n in range (5, 50,5):
    triangular=(n*(n+1))/2
    print("O triangular %i"%(triangular))
"""

#3candidatos
#total de eleitores
#cada eleitor votar e ao final mostra os votos de cada candidato.

eleitores=int(input("Digite o total de eleitores"))
candidato1=0
candidato2=0
candidato3=0
for i in range(0, eleitores, 1):
    voto=int(input("Digite o candidato, 1, 2 ou 3"))
    if voto==1:
        candidato1+=1
    elif voto==2:
        candidato2+=1
    elif voto==3:
        candidato3+=1
    else:
        print("Valor incorreto, seu voto será anulado")
print("Candidato 1: %i votos, Candidato 2: %i votos, Candidato3: %i votos"%(candidato1,candidato2,candidato3))

    
