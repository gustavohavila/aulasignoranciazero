"""

n=int(input("Digite o numero para saber se eh palindromo"))
aux,reverso = n,0

while aux !=0:
    reverso=reverso*10 +aux%10
    aux//=10

if reverso==n:
    print(n,"eh palindromo")
else:
    print(n,"nao  eh palindromo")
"""

 
