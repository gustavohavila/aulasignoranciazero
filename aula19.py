
"""n=int(input("Digite o valor de n"))
i=int(input("Digite o valor de i"))
j=int(input("Digite o valor de j"))
cont=0
soma=0
while soma<n:
    
    #print(cont)
    if cont%i==0 or cont%j==0:
        print(cont)
        soma+=1
    cont+=1
        """

i=int(input("Digite o valor de i"))
j=int(input("Digite o valor de j"))
cont=0
for a in range (0,100,1):
    if cont%i==0 and cont%j==0:
        print(cont)
    cont+=1
