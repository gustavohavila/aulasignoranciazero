
#Exercicio.
"""
n=int(input("Digite um numero:"))

soma=0
cont=1
while cont<n:
    if n%cont==0:
        soma+=cont
    cont+=1
print(soma)
if soma==n:
    print(n,"Eh perfeito")
else:
     print(n,"Nao eh perfeito")

i=1
while i*(i+1)*(i+2)<num:
    i+=1
if i*(i+1)*(i+2)!=num:
    print(num,"Nao eh perfeito")
else:
    print(num,"Eh perfeito")
n=int(input("Digite o numero de pessoas"))

cont=0
while cont<n:
    dia=int(input("Digite o dia de nascimento da pessoa %i"%(cont+1)))
    mes=int(input("Digite o mes de nascimento da pessoa %i"%(cont+1)))
    ano=int(input("Digite o ano de nascimento da pessoa %i"%(cont+1)))

    idade=int(input("Digite a idade a ser completada:"))
    print("A pessoa %i fara %i anos no dia %i/%i/%i" %(cont+1,idade, dia, mes, ano+idade))
    cont+=1

#Para inteiros --> %i ou %d
#Colocar %-->
#floats%f
#strings %s
"""
q=int(input("Digite a quantidade de numeros"))
soma=0
cont=1
while cont<q:
    n=int(input("Digite o numero %i "%(cont)))
    if cont%2==0:
        soma+=cont
    cont+=1
print("A soma dos numeros pares eh %i" %(soma))
























