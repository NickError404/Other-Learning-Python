from tkinter import  *

def calcular():
    peso1 = float(peso.get())
    altura1 = float(altura.get())

    imc = peso1/altura1**2

    resposta['text'] = f'{imc:.2f}'



janela = Tk()
janela.title('Curso de Tkinter')
janela.geometry('300x300')
janela.resizable(False, False)

Label(janela, text='Insira seu IMC').grid(row=0, column=0, columnspan=2)

Label(janela, text='Insira seu peso').grid(row=1, column=0)

peso = Entry(janela)
peso.grid(row=1, column=1)

Label(janela, text='Insira sua altura').grid(row=2, column=0)

altura = Entry(janela)
altura.grid(row=2, column=1)

Button(janela, text='Calcular', command=calcular).grid(row=3, column=0)

resposta = Label(janela, text='resposta')
resposta.grid(row=3, column=1)

janela.mainloop()