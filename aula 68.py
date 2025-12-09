#levanta um erro
#try:
#    raise ValueError
#except ValueError:
#    print('Pegamos a excessão')


#def teste():
#    try:
#        a=int(input("Escolha um número entre 1 e 20:"))
#        if not 1<= a <=20:
#            raise ValueError
#        else:
#            print('Obrigado por escolher',a)
#    except ValueError:
#        print('Entrada inválida')

class ValorRepetidoErro(Exception):
    def __init__(self,n):
        self.num=n
    def __str__(self):
        return 'Putz, meu caro, vc já digitou %i número antes'%self.num
def main():
    lista=[]

    for i in range(3):
        while True:
            try:
                num=int(input("escolha um número"))
                break
            except ValueError:
                    print('digite apenas n')
        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)
if __name__=='__main__':
    main()
