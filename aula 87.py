#aula 88


from tkinter import *

i=Tk()

i.title('Olá Mundo')
i.geometry('400x300')


texto=Label(i,text='Ola',bg='red',fg='blue')
texto.pack()

b=Button(i,text='clique')
b.pack()

ent=Entry(i)
ent.pack()

#Colocar a entrada de texto

i.mainloop()


