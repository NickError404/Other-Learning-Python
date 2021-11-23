from tkinter import  *


janela = Tk()
janela.title('Curso de Python')
janela.geometry('300x300')
janela.resizable(False, False)

Entry(janela, bg='black', fg='white', show ='*').grid(row='0', column='0',)

janela.mainloop()
