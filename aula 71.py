"""
#context manager
x=open('arquivo.txt','w')
x.write('Olá')
x.write('Mundo')
x.close
with open('arquivo.txt') as meuArquivo:
    for linha in meuArquivo:
        print(linha)
meuArquivo=open('arquivo.txt')
try:
    for linha in meuArquivo:
        print(linha)
finally:
    meuArquivo.close()


__enter__,__exit__(tipo,valor,traceback)
"""
class NossoContextManager:
    def imprime(self,msg):
        print(msg)
    def __enter__(self):
        print('Entrando no bloco with')
        return self
    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)

with NossoContextManager() as teste:
    teste.imprime('Olá Mundo')
    raise ValueError
