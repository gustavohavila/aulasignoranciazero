n=int(input("Digite o numero maluco"))
soma=0
for i in range(1,n,2):
    soma+=i
    if soma<n:
        print (soma)
        
