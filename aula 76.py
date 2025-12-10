#gerenciador de database
#modos c=create,r,n
import dbm

db=dbm.open('contatos.db', 'c')
db['Pedro']='pedro.henrique.forli@usp.br'

#tirar formato de byte
print(db['Pedro'].decode())


db['Joao']=str(13)
print(db['Joao'])

int(db['Joao'])

len(db)

db.keys() #mostra todas as chaves, em formato de bytes.


'Pedro' in db
TRUE
del db['Joao']

db['Joao']='joao@hotmail.com'

for key in db:
    print (key)

import struct
db['joao']=struct.pack('I',13)
db.close()
