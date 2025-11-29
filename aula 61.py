Pessoa={'Nome':'Lucas','Emprego':'Advogado','Idade': 20, 'Cor de Cabelo': 'Preto'}

Pessoa['Nome']='João'
Pessoa['Emprego']='Advogado'
class Pessoa:
    pass

Lucas=Pessoa()
Lucas.nome='Lucas'
Lucas.emprego='Advogado'
Lucas.CordeCabelo='Preto'
print(Lucas.__dict__)

dic=dict(nome='Lucas',emprego='Advogado', Idade=20)
print(dic)
