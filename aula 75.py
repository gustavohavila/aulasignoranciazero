#pacotes de bytes? struct
#ord('a') #=97
#x=b'palavra' #uma string representado por byte
#x[0]#112, que é igual a ord('p')

#para que usar? para usar arquivos codificados com pacotes de bytes.
#arquivos da internet.
#em arquivos avançados, criar ou lidar com esses arquivos.

#int, float.
"""
import struct #permite criar pacote de bytes.
nome='Joao'
idade=23
altura=1.7

cod=struct.pack('4s I f',nome.encode(),idade,altura)

arq=open('pessoa.cod','wb')
arq.write(cod)
arq.close()

arq=open('pessoa.cod','rb')
cod_ab=arq.readline()
cod_ab
cod_desp=struct.unpack('4s I f',cod_ab)
print(cod_desp)
Ns string de N char, I inteiro pequeno, Q inteiro grande, f float pequeno,
d float grande, ? bool

import struct
t=(b'joao',23,1.75)

s=struct.Struct('4s I f')


data=s.pack(*t)
s.unpack(data)
arq.write(
"""
