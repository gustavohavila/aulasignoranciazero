"""a=int(input("digite o primeiro"))
b=int(input("digite o primeiro"))

real=float(input("Digite o real"))

print(2*a*(b/2))
print(3*a+real)
print(real**3)
                 

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

#FORMATAÇÃO DO PRINT
a= 3.141574186486748965149684
print("Gustavo %10.500f"%a)
"""
salario=int(input("Digite o salário "))
salarioanterior=salario
print("Salário antes do reajuste: %i "%salario)
percentual=0
if salario <=280:
    percentual=1.20
    salario=salario*percentual
elif salario >280 and salario <=700:
    percentual=1.15
    salario *=percentual
elif salario >700 and salario<=1500:
    percentual=1.10
    salario*=percentual
elif salario >1500:
    percentual=1.05
    salario*=percentual

print("o percentual do salário aplicado foi ", percentual)

print("O valor do aumento foi de: %i "%(salario-salarioanterior))

print("O valor do novo salário é:", salario)
