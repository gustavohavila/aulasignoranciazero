from tkinter import *

def Calcular():
    resultado['text']=form.get()
    resultado['fg']='green'


#cria nossa tela
instancia=Tk()

#dá um título para tela
instancia.title('calculadora para estatística')

#dá um tamanho a tela
instancia.geometry('800x600')

#coloca a entrada de texto
form=Entry(instancia)
form.pack()

#botão calcular
calc=Button(instancia,text='calcule', fg='green',bg='red',command=Calcular)
calc.pack()

#texto das fórmulas
resultado=Label(instancia,text='Resultado',fg='blue')
resultado.pack()

#inicia o programa
instancia.mainloop()
