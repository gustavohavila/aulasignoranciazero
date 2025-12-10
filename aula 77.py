#JSON - javascript object notation serializer=json
#javascript usada para websites

import json
data1={'Nome':'Pedro','RG':123456789, 'CPF':12345678910}
data_string = json.dumps(data1)
print(data_string)
file=open('test.json','wb')
data2=[1,2,3,4]
data3='a','b','c'
data_s2=json.dumps(data2)
data_s3=json.dumps(data3)
file.write(data_string.encode())
file.write(data_s2.encode())
file.write(data_s3.encode())
file.close
file=open('test.json','rb')
data_total=file.readline()
data1=data_total[:54]
data2=data_total[54:66]
data2=data2.decode()
obj1=json.loads(data1)
obj2=json.loads(data2)
data3=data_total[66:]
data3=data3.decode()
obj3=json.loads(data3)
print(data3)

class Pessoa:
    pass

data_s=json.dumps(Pessoa())

#acima não dá certo

a=Pessoa()
a.__dict__ #posso usar esse dicionario para jogar no jason.
#javascript não tem tupla, então é recomendado usar sempre listas, ou fique ciente que ele vai sempre retornar listas.

a['class']=True
