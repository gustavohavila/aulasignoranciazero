#all

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

#any --> algum

any([0,0,0])

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

#sum --> soma
#sum('abcd')


#reduce

import functools

def olhe_soma(x,y):
    print('Adicionando', x, 'a',y)
    return x+y

print(functools.reduce(olhe_soma, [1,2,3,4,5]))

