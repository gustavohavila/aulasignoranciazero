"""
i=0
n=5

while i<n:
    j=0
    while j<n:
        print(i,j)
        j=j+1
    print(i)
    i=i+1
"""

n=int(input("Digite o numero de empresas: "))
m=int(input("Digite o numero de meses: "))
        
empresa=1
print("")
while empresa<=n:
    mes=1
    balanca=0
    print("Empresa",empresa, ":")
    while mes<=m:
        print("Mes",mes,":")
        ganho=int(input("Digite o ganho da empresa no mes: "))
        gasto=int(input("Digite o gasto da empreasa no mes: "))
        balanca=balanca+(ganho-gasto)
        print("")
        mes=mes+1
    if balanca ==0:
        print("A empresa", empresa,"ficou indiferente")
    elif balanca >0:
        print("A empresa",empresa, "fechou com lucro de R$",balanca)
    else:
        print("A empresa", empresa,"fechou com deficit de R$", balanca)
    empresa=empresa+1 
    print("")
