area=int(input("Digite a área a ser pintada\n"))

area=area+(area*0.10)

print("Área com 10% de folga", area)
litro=area//6 #define 1 litro a cada 6m de area

print("Quantidade de litros", litro)

lata=litro//18

galao=litro//4

print("resto da divisão de litros por lata", litro%18)

if litro%18>0:
    if litro%18<=4:
        print("Total de latas:",lata,"total de galao:",1,"valor:", lata*80+25)
        
    if litro%18>4:
        print("Total de latas:",lata,"total de galao:",2,"valor:", lata*80+50)
        
    if litro%18<=12:
        print("Total de latas:",lata,"total de galao:",3,"valor:", lata*80+75)
        
    else:
        print("Total de latas:",lata+1,"total de galao:",0,"valor:", (lata+1)*80)

print("somente latas", lata, "preço das latas:", lata*80)
print("Somente galão", galao, "preço dos galões:",galao*25)
