a=float(input("Digite o valor de a"))
b=float(input("Digite o valor de b"))
c=float(input("Digite o valor de c"))

delta=b**2-(4*a*c)

raiz=((-b +(delta**(1/2)))/2*a)
raiz1=((-b -(delta**(1/2)))/2*a)

if a==0:
    print('programa deu pau')
elif delta<0:
    print("não possui raizes reais")
elif delta==0:
    print("apenas uma raiz real",raiz)
elif delta>0:
    print("Duas raizes", raiz, raiz1)
