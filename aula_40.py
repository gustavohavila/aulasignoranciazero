#nested functions
#nested - repetições entre chaves.
#uma função dentro de outra função.

def exp(N):
    def eleva (X):
        print(X**N)
    return eleva
f=exp(3)
f(2)
