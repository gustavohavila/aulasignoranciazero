#excessões
#try:
#    int('fdsa')
#except:
#    print('deu ruim')


#outro exemplo
try:
    x=int(input('digite um número'))
    print(x)
except:
    print('Deu erro!')
    x=0
finally:
    print(x)


#
try:
    a=open('arquivo.txt','r')
    linha=a.readline()
    linha.split('!')
    linha=linha[400]
    a.close()
    a=open('arquivo.txt','w')
    a.write(linha)
except FileNotFoundError:
    a=open('arquivo.txt','w')
    a.write('ERRO!')
    print('deu erro')
finally:
    a.close()
