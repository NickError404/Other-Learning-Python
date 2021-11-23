
from tkinter import  *

class cliques():

    def click():
        armazenarLabel['text'] = 'click me'

    def clicked():
        armazenarLabel['text'] = 'click has been clicked'

janela = Tk()
janela.title('Curso de Tkinter')
janela.geometry('300x300')
janela.resizable(False, False)

Button(janela, bg='cyan', fg='white', text='Clique aqui', height=5, width=10, command=cliques.click).grid(row=0, column=2)

armazenarLabel = Label(janela, text='Click me')
armazenarLabel.grid(row=1, column=2)

Button(janela, bg='black', fg='white', text='Agora clique aqui', height=5, width=10, command=cliques.clicked).grid(row=2, column=2)

janela.mainloop()