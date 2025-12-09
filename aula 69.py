#clausulas em um bloco try
"""
try:
 lista=[]
 try:
     lista.append(int('dsag'))
 a=lista[0]
except IndexError:
    print('erro')
except ValueError:
    print('deu erro de valor')
finally:
    print('chegamos ao final')
"""
try:
    lista=[]
    lista.append(int('dsag'))
    print('vamo time')
except (IndexError, ValueError) as (excessao,x):
    excessao
    print('Erro')
finally:
    print('Chegamos ao final')

#resumindo
    #try
    #except nome
    #except (nome1,nome2)
    #except (nome1,nome2,...) as valor
    #except
    #else
    #finaly
