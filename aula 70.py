#excessões encadeadas
#num=1/0
#int(num)

#try:
#    num=1/0
#    int(num)
#except Exception as E:
#    raise ValueError from E

while True:
    try:
        num=int(input("Digite um número entre 1 e 20:"))
    except ValueError:
        print("digite apenas números")
    except:
        print('Entrada Inválida')
    else:
        break
test=True

if not 1<=num<=20:
    test=False
assert test, num

if __debug__:
    if not test:
        raise AssertionError(num)

#exemplo do assert

def fazer(x):
    assert x>0
    return x**1/2
