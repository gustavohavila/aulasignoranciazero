
"""FAÇA UM PROGRAMA PARA UMA LOJA DE TINTAS. O PROGRAMA DEVERÁ PEDIR O TAMANHO EM METROS QUADRADOS DA ÁREA A SER PINTADA.
CONSIDERE QUE A COBERTURA DA TINTA É DE 1 LITRO PARA CADA 6METROS QUADRADOS E QUE A TINTA É VENDIDA EM LATAS DE 18 LITROS.
QUE CUSTAM 80 REAIS OU 25 REAIS.

APENAS LATAS
APENAS GALOES
MISTURAR LATAS E GALOES, DE FORMA QUE O PREÇO SEJA MENOR.
"""
area=int(input("Digite a área a ser pintada\n"))
#colocando já  afolga de 10%

area= area+area*0.10

print(area)

litro=area//6  #define 1 litro a cada 6 m de área

print("Quantidade de litros",litro)
lata=litro//18

galao=litro//4
mistura=0   #número de latas que precisam sobrar para ser benéfico o preço.

print("o resto da divisão por 18 é",litro%18)
if litro%18>0:
    lata=lata+1
    print("Somente latas", lata,"R$",lata*80)
    if litro%18<4:
        lata=lata-1
        mistura=1
    else:
        lata=lata-1
        mistura=2
else:
    print("Somente latas", lata,"R$",lata*80)

        
if litro%4>0:
    galao=galao+1



print("Somente galao",galao,"R$",galao*25)



#misturar latas e galões
print("latas", lata, "preço lata", (lata)*80,"galao",mistura,"preço galao", mistura*25,
      "preço total",mistura*25+(lata)*80)


    
    
