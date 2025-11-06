#nested for loops.
#for i in range (3):
#    for j in range (0,3,2):
#        print(i,j)
#Exercicio

inicio=int(input("Digite o início da tabuada"))
fim=int(input("Digite o fim da tabuada"))

for i in range (1,fim+1):
    for j in range (fim+1):
        print("%i X %i = %i"%(i,j,i*j))
    print("")
        
