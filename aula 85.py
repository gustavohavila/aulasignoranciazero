#gerador

g=(x**2 for x in range(10) if x%2==0)

iter(g) is g

for i in g:
    print(i)

 
list(g) #limitação

list((x**2 for  x in range(10) if x%2==0))

map,filter
