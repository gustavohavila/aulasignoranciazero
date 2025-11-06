"""a=int(input("digite o primeiro"))
b=int(input("digite o primeiro"))

real=float(input("Digite o real"))

print(2*a*(b/2))
print(3*a+real)
print(real**3)
                 
"""
n1=float(input(("Digite um numero")))




if n1!=int(n1):
    decimal=n1-int(n1)
    arredondado= int(n1)
    if decimal >=0.5:
        arredondado+=1
    print("Arredondando", arredondado)
    print("inteiro")
else:
    print("é decimal")
print(n1)
